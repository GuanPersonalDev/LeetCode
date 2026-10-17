from leetviz import trace_solution

trace_solution(
    title="貪婪分層",
    source="implement_45.py",
    method="Solution.jump",
    cases={
        "範例 1": {"nums": [2, 3, 1, 1, 4]},
        "範例 2": {"nums": [2, 3, 0, 1, 4]},
    },
    arrays={"nums": ["i", "current_jump_limit", "farthest_index"]},
    scalars=["step_count"],
    notes={
        "farthest_index = max(farthest_index, i + nums[i])": "更新下一跳最遠能到哪",
        "if i == current_jump_limit:": "是否走到這一跳的邊界",
        "current_jump_limit = farthest_index": "到邊界了：多跳一次，邊界推到最遠處",
    },
    out="45/greedy_bfs",
)
