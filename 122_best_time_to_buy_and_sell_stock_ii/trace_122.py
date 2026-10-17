from leetviz import trace_solution

trace_solution(
    title="累加每段上漲",
    source="implement_122.py",
    method="Solution.maxProfit",
    cases={
        "範例 1": {"prices": [7, 1, 5, 3, 6, 4]},
        "範例 2": {"prices": [1, 2, 3, 4, 5]},
    },
    arrays={"prices": ["i"]},
    scalars=["profit"],
    notes={
        "if prices[i] > prices[i-1]:": "今天比昨天高嗎",
        "profit += prices[i] - prices[i-1]": "上漲：把這一天的漲幅吃下來",
    },
    out="122/sum_rises",
)
