from leetviz import trace_solution

trace_solution(
    title="左右兩趟乘積",
    source="implement_238.py",
    method="Solution.productExceptSelf",
    cases={
        "範例 1": {"nums": [1, 2, 3, 4]},
        "範例 2": {"nums": [-1, 1, 0, -3, 3]},
    },
    arrays={"nums": ["i"], "answer": ["i"]},
    scalars=["left_product", "right_product"],
    notes={
        "answer[i] = left_product": "第一趟：先放 i 左邊所有數的乘積",
        "answer[i] *= right_product": "第二趟：再乘上 i 右邊所有數的乘積",
    },
    out="238/prefix_suffix",
)
