from leetviz import trace_solution

trace_solution(
    title="記住最低價",
    source="implement_121.py",
    method="Solution.maxProfit",
    cases={
        "範例 1": {"prices": [7, 1, 5, 3, 6, 4]},
        "範例 2": {"prices": [7, 6, 4, 3, 1]},
    },
    arrays={"prices": []},
    scalars=["p", "min_price", "new_profit", "max_profit"],
    notes={
        "min_price = p": "出現更低的價格：更新最低買入價",
        "new_profit = p - min_price": "如果今天賣出，能賺多少",
        "max_profit = new_profit": "比目前最佳獲利更好，更新",
    },
    out="121/track_min",
)
