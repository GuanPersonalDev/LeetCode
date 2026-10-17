from leetviz import trace_solution

trace_solution(
    title="快慢指標",
    source="implement_26.py",
    method="Solution.removeDuplicates",
    cases={
        "基本：[1,1,2]": {"nums": [1, 1, 2]},
        "邊界：單一元素": {"nums": [1]},
        "邊界：全部相同": {"nums": [1, 1, 1]},
        "複雜：官方範例 2": {"nums": [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]},
    },
    arrays={"nums": ["result_index", "i"]},
    scalars=[],
    notes={
        "if nums[result_index] != nums[i]:": "比較目前的值和結果區的最後一個",
        "nums[result_index] = nums[i]": "出現新數字：寫進結果區的下一格",
    },
    out="26/two_pointers",
)
