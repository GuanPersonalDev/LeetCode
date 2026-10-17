from leetviz import trace_solution

trace_solution(
    title="字串累加",
    source="implement_412.py",
    method="Solution.fizzBuzz",
    cases={
        "n = 15": {"n": 15},
    },
    arrays={"result": []},
    scalars=["i", "str"],
    notes={
        "str += \"Fizz\"": "3 的倍數：接上 Fizz",
        "str += \"Buzz\"": "5 的倍數：接上 Buzz",
        "str = f'{i}'": "都不是：放數字本身",
    },
    out="412/concat",
)
