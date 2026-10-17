"""執行所有題目資料夾下的 trace_*.py，產生網站用的 JSON。"""
import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    scripts = sorted(ROOT.glob("[0-9]*_*/trace_*.py"))
    for script in scripts:
        print(f"trace: {script.relative_to(ROOT)}")
        runpy.run_path(str(script), run_name="__main__")
    print(f"done: {len(scripts)} script(s)")
    return 0


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT))
    sys.exit(main())
