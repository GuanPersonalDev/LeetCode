from leetviz import trace_solution

trace_solution(
    title="模擬",
    source="implement_1342.py",
    method="Solution.numberOfSteps",
    cases={
        "num = 14": {"num": 14},
        "num = 123": {"num": 123},
    },
    arrays={},
    scalars=["num", "count"],
    notes={
        "num = num / 2": "偶數：除以 2",
        "num = num - 1": "奇數：減 1",
    },
    out="1342/simulate",
)
