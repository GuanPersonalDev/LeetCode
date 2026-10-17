from leetviz import trace_solution

trace_solution(
    title="逐列加總",
    source="implement_1672.py",
    method="Solution.maximumWealth",
    cases={
        "範例 1": {"accounts": [[1, 2, 3], [3, 2, 1]]},
        "範例 2": {"accounts": [[2, 8, 7], [7, 1, 3], [1, 9, 5]]},
    },
    arrays={"moneys": []},
    scalars=["v", "sum", "max"],
    notes={
        "sum += v": "加總這位客戶的存款",
        "max = sum": "比目前最富有的還多，更新",
    },
    out="1672/row_sum",
)
