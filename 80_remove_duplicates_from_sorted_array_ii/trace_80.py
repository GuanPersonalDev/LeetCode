from leetviz import trace_solution

trace_solution(
    title="與倒數第二個比較",
    source="implement_80.py",
    method="Solution.removeDuplicates",
    cases={
        "基本：[1,1,1,2,2,3]": {"nums": [1, 1, 1, 2, 2, 3]},
        "邊界：單一元素": {"nums": [1]},
        "邊界：全部相同": {"nums": [1, 1, 1, 1]},
        "複雜：官方範例 2": {"nums": [0, 0, 1, 1, 1, 1, 2, 3, 3]},
    },
    arrays={"nums": ["current_index"]},
    scalars=["n"],
    notes={
        "if current_index < 2 or n > nums[current_index - 2]:": "跟結果區倒數第二個比，判斷會不會出現第三次",
        "nums[current_index] = n": "保留：寫進結果區",
    },
    out="80/compare_second_last",
)
