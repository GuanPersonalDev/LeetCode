from leetviz import trace_solution

trace_solution(
    title="由後往前合併",
    source="implement_88.py",
    method="Solution.merge",
    cases={
        "基本：官方範例 1": {"nums1": [1, 2, 3, 0, 0, 0], "m": 3, "nums2": [2, 5, 6], "n": 3},
        "邊界：nums2 為空": {"nums1": [1], "m": 1, "nums2": [], "n": 0},
        "邊界：nums1 為空": {"nums1": [0], "m": 0, "nums2": [1], "n": 1},
        "複雜：含負數與重複": {"nums1": [-1, 0, 0, 3, 3, 3, 0, 0, 0], "m": 6, "nums2": [1, 2, 2], "n": 3},
    },
    arrays={"nums1": ["current_index", "nums1_progress"], "nums2": ["nums2_progress"]},
    scalars=["a", "b"],
    notes={
        "if a > b:": "比較兩邊還沒放的最大值",
        "nums1[current_index] = a": "nums1 的比較大，放到最後面",
        "nums1[current_index] = b": "nums2 的比較大（或相等），放到最後面",
        "nums1[current_index] = nums2[nums2_progress]": "nums1 已經用完，直接搬 nums2",
    },
    out="88/merge_from_back",
)
