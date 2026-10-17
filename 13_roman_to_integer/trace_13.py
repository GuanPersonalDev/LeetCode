from leetviz import trace_solution

trace_solution(
    title="相鄰比較",
    source="implement_13.py",
    method="Solution.romanToInt",
    cases={
        "基本：XIV": {"s": "XIV"},
        "邊界：單一符號 I": {"s": "I"},
        "邊界：最大值 MMMCMXCIX": {"s": "MMMCMXCIX"},
        "複雜：LVIII": {"s": "LVIII"},
        "複雜：MCMXCIV": {"s": "MCMXCIV"},
    },
    arrays={"s": ["i"]},
    scalars=["total"],
    notes={
        "total -= roman_list[s[i]]": "下一個符號比較大：這個符號屬於減法組合，扣掉",
        "total += roman_list[s[i]]": "下一個符號不比較大：直接加上",
    },
    out="13/compare_next",
)
