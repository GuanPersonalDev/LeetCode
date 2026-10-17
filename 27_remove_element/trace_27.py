from leetviz import trace_solution

trace_solution(
    title="覆寫保留",
    source="implement_27.py",
    method="Solution.removeElement",
    cases={
        "基本：[3,2,2,3] 移除 3": {"nums": [3, 2, 2, 3], "val": 3},
        "邊界：空陣列": {"nums": [], "val": 0},
        "邊界：全部移除": {"nums": [2, 2], "val": 2},
        "邊界：沒有要移除的": {"nums": [1], "val": 2},
        "複雜：官方範例 2": {"nums": [0, 1, 2, 2, 3, 0, 4, 2], "val": 2},
    },
    arrays={"nums": ["i", "result_len"]},
    scalars=["n", "val"],
    notes={
        "if n != val:": "不是要移除的值才保留",
        "nums[result_len] = n": "寫到保留區的下一格",
    },
    out="27/overwrite",
)
