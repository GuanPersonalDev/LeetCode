from leetviz import trace_solution

trace_solution(
    title="剩餘步數",
    source="implement_55.py",
    method="Solution.canJump",
    cases={
        "基本：可到達": {"nums": [2, 3, 1, 1, 4]},
        "基本：卡在 0": {"nums": [3, 2, 1, 0, 4]},
        "邊界：單一元素": {"nums": [0]},
        "邊界：起點就是 0": {"nums": [0, 1]},
        "複雜：[2,5,0,0]": {"nums": [2, 5, 0, 0]},
        "複雜：[1,1,2,0,0,1]": {"nums": [1, 1, 2, 0, 0, 1]},
    },
    arrays={"nums": []},
    scalars=["n", "s"],
    notes={
        "if s < 0:": "剩餘步數是否已經不夠走到這一格",
        "s = n": "這一格的跳躍力比較大，改用它",
        "s -= 1": "往下一格走，消耗一步",
    },
    out="55/remaining_steps",
)
