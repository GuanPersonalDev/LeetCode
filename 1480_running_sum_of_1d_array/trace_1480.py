from leetviz import trace_solution

trace_solution(
    title="原地累加",
    source="implement_1480.py",
    method="Solution.runningSum",
    cases={
        "基本：[1,2,3,4]": {"nums": [1, 2, 3, 4]},
        "邊界：單一元素": {"nums": [1]},
        "邊界：含負數": {"nums": [-1, -2, 3]},
        "複雜：[3,1,2,10,1]": {"nums": [3, 1, 2, 10, 1]},
    },
    arrays={"nums": ["i"]},
    scalars=[],
    notes={
        "nums[i] += nums[i-1]": "加上前一格（前一格已經是前綴和）",
    },
    out="1480/in_place",
)
