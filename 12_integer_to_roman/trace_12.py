from leetviz import trace_solution

trace_solution(
    title="逐位數轉換",
    source="implement_12.py",
    method="Solution.intToRoman",
    cases={
        "基本：14": {"num": 14},
        "邊界：最小值 1": {"num": 1},
        "邊界：最大值 3999": {"num": 3999},
        "複雜：官方範例 3749": {"num": 3749},
        "複雜：官方範例 58": {"num": 58},
        "複雜：官方範例 1994": {"num": 1994},
    },
    arrays={"palces": []},
    scalars=["num", "value", "d", "result"],
    notes={
        "d = num // value": "取出目前這一位的數字",
        "num %= value": "把這一位從 num 去掉，留給下一位處理",
        "result += one + ten": "這一位是 9：小的符號放在十的左邊，例如 CM",
        "result += five + one * (d-5)": "這一位是 5～8：先放五，再補 d-5 個一",
        "result += one + five": "這一位是 4：小的符號放在五的左邊，例如 CD",
        "result += one * d": "這一位是 0～3：重複 d 個一，0 時不加任何字",
    },
    out="12/digit_by_digit",
)
