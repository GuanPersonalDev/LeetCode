from leetviz import trace_solution

trace_solution(
    title="覆寫保留",
    source="implement_27.py",
    method="Solution.removeElement",
    cases={
        "範例 1": {"nums": [3, 2, 2, 3], "val": 3},
        "範例 2": {"nums": [0, 1, 2, 2, 3, 0, 4, 2], "val": 2},
    },
    arrays={"nums": ["i", "result_len"]},
    scalars=["n", "val"],
    notes={
        "if n != val:": "不是要移除的值才保留",
        "nums[result_len] = n": "寫到保留區的下一格",
    },
    out="27/overwrite",
)
