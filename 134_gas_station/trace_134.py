from leetviz import trace_solution

trace_solution(
    title="油箱歸零換起點",
    source="implement_134.py",
    method="Solution.canCompleteCircuit",
    cases={
        "基本：官方範例 1": {"gas": [1, 2, 3, 4, 5], "cost": [3, 4, 5, 1, 2]},
        "邊界：只有一站": {"gas": [2], "cost": [2]},
        "邊界：總油量不足": {"gas": [2, 3, 4], "cost": [3, 4, 3]},
        "複雜：[5,8,2,8]": {"gas": [5, 8, 2, 8], "cost": [6, 5, 6, 6]},
        "複雜：起點是第 0 站": {"gas": [3, 1, 1], "cost": [1, 2, 2]},
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
