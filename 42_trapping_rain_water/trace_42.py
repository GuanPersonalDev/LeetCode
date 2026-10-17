from leetviz import trace_solution

trace_solution(
    title="雙指標",
    source="implement_42.py",
    method="Solution.trap",
    cases={
        "基本：[2,0,2]": {"height": [2, 0, 2]},
        "邊界：單一柱子": {"height": [4]},
        "邊界：遞增接不到水": {"height": [1, 2, 3]},
        "複雜：官方範例 1": {"height": [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]},
        "複雜：官方範例 2": {"height": [4, 2, 0, 3, 2, 5]},
    },
    arrays={"height": ["left_index", "right_index"]},
    scalars=["left_max", "right_max", "total"],
    notes={
        "if left_max < right_max:": "比較兩側目前的最高牆，較矮的那一側才能確定水位",
        "left_index += 1": "左側較矮：左指標往右移",
        "total += left_max - height[left_index]": "這一格的水位由 left_max 決定，累加 left_max - 牆高",
        "right_index -= 1": "右側較矮（或相等）：右指標往左移",
        "total += right_max - height[right_index]": "這一格的水位由 right_max 決定，累加 right_max - 牆高",
    },
    out="42/two_pointers",
)
