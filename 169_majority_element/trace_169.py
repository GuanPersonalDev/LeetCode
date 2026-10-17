from leetviz import trace_solution

trace_solution(
    title="投票抵銷",
    source="implement_169.py",
    method="Solution.majorityElement",
    cases={
        "基本：[3,2,3]": {"nums": [3, 2, 3]},
        "邊界：單一元素": {"nums": [1]},
        "複雜：官方範例 2": {"nums": [2, 2, 1, 1, 1, 2, 2]},
    },
    arrays={"nums": []},
    scalars=["i", "num", "counter"],
    notes={
        "num = i": "票數歸零：換這個數當候選人",
        "counter += 1 if num == i else -1": "跟候選人相同加一票，不同就抵銷一票",
    },
    out="169/boyer_moore",
)
