from leetviz import trace_solution

trace_solution(
    title="三次反轉",
    source="implement_189.py",
    method="Solution.rotate",
    cases={
        "基本：官方範例 1": {"nums": [1, 2, 3, 4, 5, 6, 7], "k": 3},
        "邊界：k = 0": {"nums": [1, 2, 3], "k": 0},
        "邊界：k 大於長度": {"nums": [1, 2], "k": 3},
        "複雜：含負數": {"nums": [-1, -100, 3, 99], "k": 2},
    },
    arrays={"nums": []},
    scalars=["n", "k"],
    notes={
        "self.reverse(nums, 0, n-1)": "第一次：整個陣列反轉",
        "self.reverse(nums, 0, k-1)": "第二次：反轉前 k 個",
        "self.reverse(nums, k, n-1)": "第三次：反轉剩下的",
    },
    out="189/three_reverses",
)
