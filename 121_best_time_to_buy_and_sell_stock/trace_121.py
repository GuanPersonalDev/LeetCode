from leetviz import trace_solution

trace_solution(
    title="記住最低價",
    source="implement_121.py",
    method="Solution.maxProfit",
    cases={
        "基本：官方範例 1": {"prices": [7, 1, 5, 3, 6, 4]},
        "邊界：只有一天": {"prices": [5]},
        "邊界：一路下跌": {"prices": [7, 6, 4, 3, 1]},
        "複雜：最低價出現在後段": {"prices": [3, 2, 6, 5, 0, 3]},
        "複雜：[2,4,1,7,0,6]": {"prices": [2, 4, 1, 7, 0, 6]},
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
