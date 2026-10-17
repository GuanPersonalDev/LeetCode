"""用 sys.settrace 執行使用者的解法，逐行錄下區域變數，輸出給 TraceViewer 播放的 JSON。"""
from __future__ import annotations

import contextlib
import copy
import importlib.util
import inspect
import io
import json
import sys
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "public" / "traces"
MAX_STEPS = 1000


class TraceError(Exception):
    pass


def _load_module(path: Path):
    spec = importlib.util.spec_from_file_location(f"leetviz_src_{path.parent.name}", path)
    module = importlib.util.module_from_spec(spec)
    # 解法檔尾有 print 測試，載入時把輸出吞掉
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


def _resolve(module, method: str) -> tuple[Callable, Any]:
    """'Solution.trap' → (綁定好的方法, 原始函式)。"""
    class_name, _, func_name = method.partition(".")
    if not func_name:
        func = getattr(module, class_name)
        return func, func
    cls = getattr(module, class_name)
    func = getattr(cls, func_name)
    return getattr(cls(), func_name), func


def _jsonable(value: Any) -> Any:
    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    if isinstance(value, (list, tuple)):
        return [_jsonable(v) for v in value]
    if isinstance(value, (set, frozenset)):
        return sorted((_jsonable(v) for v in value), key=repr)
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    return repr(value)


def _snapshot(frame_locals: dict) -> dict:
    snap = {}
    for name, value in frame_locals.items():
        if name == "self":
            # 設計題的狀態放在 self 上，展開成 self.xxx
            for attr, attr_value in vars(value).items():
                snap[f"self.{attr}"] = _jsonable(attr_value)
            continue
        snap[name] = _jsonable(value)
    return snap


def _run_case(bound: Callable, func, args: dict) -> tuple[list[dict], Any]:
    code = func.__code__
    steps: list[dict] = []

    def local_trace(frame, event, arg):
        if event == "line":
            if len(steps) >= MAX_STEPS:
                raise TraceError(f"超過 {MAX_STEPS} 步，請改用較小的輸入")
            steps.append({"line": frame.f_lineno, "vars": _snapshot(frame.f_locals)})
        elif event == "return":
            steps.append({"line": frame.f_lineno, "vars": _snapshot(frame.f_locals), "return": _jsonable(arg)})
        return local_trace

    def global_trace(frame, event, arg):
        # 只追目標方法本身；它呼叫的其他函式不展開
        if event == "call" and frame.f_code is code:
            return local_trace
        return None

    call_args = copy.deepcopy(args)
    sys.settrace(global_trace)
    try:
        result = bound(**call_args)
    finally:
        sys.settrace(None)
    return steps, _jsonable(result)


def trace_solution(
    *,
    source: str,
    method: str,
    cases: dict[str, dict],
    out: str,
    title: str = "",
    arrays: dict[str, list[str]] | None = None,
    scalars: list[str] | None = None,
    notes: dict[str, str] | None = None,
) -> Path:
    """
    追蹤 source 裡的 method，對每個 case 錄下逐行狀態，寫到 public/traces/<out>.json。

    source 相對於呼叫者（trace_*.py）所在的資料夾；arrays 是「陣列變數 → 指在它上面的指標變數」；
    notes 以原始碼那一行去掉縮排後的文字對應說明。
    """
    caller = Path(inspect.stack()[1].filename).resolve().parent
    source_path = (caller / source).resolve()
    if not source_path.exists():
        raise TraceError(f"找不到解法檔：{source_path}")

    bound, func = _resolve(_load_module(source_path), method)
    lines = source_path.read_text(encoding="utf-8").splitlines()
    notes = notes or {}
    unknown = [text for text in notes if not any(line.strip() == text for line in lines)]
    if unknown:
        raise TraceError(f"notes 對不到原始碼的行：{unknown}")

    traced_cases = {}
    for name, args in cases.items():
        steps, result = _run_case(bound, func, args)
        for step in steps:
            note = notes.get(lines[step["line"] - 1].strip())
            if note:
                step["note"] = note
        traced_cases[name] = {"input": _jsonable(args), "result": result, "steps": steps}

    first, last = func.__code__.co_firstlineno, func.__code__.co_firstlineno + len(inspect.getsource(func).splitlines()) - 1
    data = {
        "title": title or method,
        "source": source_path.relative_to(ROOT).as_posix() if source_path.is_relative_to(ROOT) else source_path.name,
        "code": lines,
        "range": [first, last],
        "view": {"arrays": arrays or {}, "scalars": scalars or []},
        "cases": traced_cases,
    }
    out_path = OUTPUT_DIR / f"{out}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return out_path
