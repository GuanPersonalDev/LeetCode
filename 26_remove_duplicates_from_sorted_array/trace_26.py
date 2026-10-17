from leetviz import trace_solution

trace_solution(
    title="快慢指標",
    source="implement_26.py",
    method="Solution.removeDuplicates",
    cases={
        "範例 1": {"nums": [1, 1, 2]},
        "範例 2": {"nums": [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]},
    },
    arrays={"nums": ["result_index", "i"]},
    scalars=[],
    notes={
        "if nums[result_index] != nums[i]:": "比較目前的值和結果區的最後一個",
        "nums[result_index] = nums[i]": "出現新數字：寫進結果區的下一格",
    },
    out="26/two_pointers",
)
