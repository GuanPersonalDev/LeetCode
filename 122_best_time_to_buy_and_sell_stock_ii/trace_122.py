from leetviz import trace_solution

trace_solution(
    title="累加每段上漲",
    source="implement_122.py",
    method="Solution.maxProfit",
    cases={
        "基本：官方範例 1": {"prices": [7, 1, 5, 3, 6, 4]},
        "邊界：只有一天": {"prices": [1]},
        "邊界：一路下跌": {"prices": [5, 4, 3]},
        "複雜：持平與多段上漲": {"prices": [3, 3, 5, 0, 0, 3, 1, 4]},
    },
    arrays={"prices": ["i"]},
    scalars=["profit"],
    notes={
        "if prices[i] > prices[i-1]:": "今天比昨天高嗎",
        "profit += prices[i] - prices[i-1]": "上漲：把這一天的漲幅吃下來",
    },
    out="122/sum_rises",
)
