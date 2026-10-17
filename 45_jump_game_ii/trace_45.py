from leetviz import trace_solution

trace_solution(
    title="貪婪分層",
    source="implement_45.py",
    method="Solution.jump",
    cases={
        "基本：[2,3,1,1,4]": {"nums": [2, 3, 1, 1, 4]},
        "邊界：單一元素": {"nums": [0]},
        "邊界：每格只能跳 1": {"nums": [1, 1, 1]},
        "複雜：[2,3,0,1,4]": {"nums": [2, 3, 0, 1, 4]},
        "複雜：[5,9,3,2,1,0,2,3,3,1,0,0]": {"nums": [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]},
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
