from leetviz import trace_solution

trace_solution(
    title="計數",
    source="implement_274.py",
    method="Solution.hIndex",
    cases={
        "範例 1": {"citations": [3, 0, 6, 1, 5]},
        "範例 2": {"citations": [1, 3, 1]},
    },
    arrays={"citations": [], "counter": ["i"]},
    scalars=["c", "cited_count"],
    notes={
        "counter[min(c, counter_max_index)] += 1": "被引用 c 次的論文數 +1（超過 n 次算在最後一格）",
        "cited_count += counter[i]": "累加被引用至少 i 次的論文數",
        "if cited_count >= i:": "至少 i 篇被引用至少 i 次 → h 就是 i",
    },
    out="274/counting",
)
