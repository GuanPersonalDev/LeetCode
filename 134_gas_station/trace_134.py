from leetviz import trace_solution

trace_solution(
    title="油箱歸零換起點",
    source="implement_134.py",
    method="Solution.canCompleteCircuit",
    cases={
        "範例 1": {"gas": [1, 2, 3, 4, 5], "cost": [3, 4, 5, 1, 2]},
        "範例 2": {"gas": [5, 8, 2, 8], "cost": [6, 5, 6, 6]},
    },
    arrays={"gas": ["i", "start_index"], "cost": ["i"]},
    scalars=["tank"],
    notes={
        "tank += gas[i] - cost[i]": "加這一站的油、扣掉開往下一站的油",
        "start_index = i+1": "油箱變負：前面的站都不能當起點，改從下一站開始",
        "if sum(cost) > sum(gas):": "總油量不夠就不可能繞完",
    },
    out="134/reset_start",
)
