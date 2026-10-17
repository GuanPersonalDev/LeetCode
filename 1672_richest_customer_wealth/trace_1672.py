from leetviz import trace_solution

trace_solution(
    title="逐列加總",
    source="implement_1672.py",
    method="Solution.maximumWealth",
    cases={
        "基本：兩位客戶": {"accounts": [[1, 2, 3], [3, 2, 1]]},
        "邊界：一位客戶一家銀行": {"accounts": [[5]]},
        "複雜：[[1,5],[7,3],[3,5]]": {"accounts": [[1, 5], [7, 3], [3, 5]]},
        "複雜：官方範例 3": {"accounts": [[2, 8, 7], [7, 1, 3], [1, 9, 5]]},
    },
    arrays={"moneys": []},
    scalars=["v", "sum", "max"],
    notes={
        "sum += v": "加總這位客戶的存款",
        "max = sum": "比目前最富有的還多，更新",
    },
    out="1672/row_sum",
)
