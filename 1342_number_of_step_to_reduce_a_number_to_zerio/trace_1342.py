from leetviz import trace_solution

trace_solution(
    title="模擬",
    source="implement_1342.py",
    method="Solution.numberOfSteps",
    cases={
        "基本：14": {"num": 14},
        "邊界：0": {"num": 0},
        "邊界：1": {"num": 1},
        "複雜：123": {"num": 123},
    },
    arrays={},
    scalars=["num", "count"],
    notes={
        "num = num / 2": "偶數：除以 2",
        "num = num - 1": "奇數：減 1",
    },
    out="1342/simulate",
)
