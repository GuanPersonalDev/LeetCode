from leetviz import trace_solution

trace_solution(
    title="上下坡計數",
    source="implement_135.py",
    method="Solution.candy",
    cases={
        "範例 1": {"ratings": [1, 0, 2]},
        "範例 2": {"ratings": [1, 2, 2]},
        "山形": {"ratings": [1, 3, 4, 5, 2]},
    },
    arrays={"ratings": ["i"]},
    scalars=["increase_step", "decrease_step", "total_count"],
    notes={
        "total_count += increase_step": "上坡：這個位置要比起點多 increase_step 顆",
        "total_count += decrease_step": "下坡：從坡底往回數，多 decrease_step 顆",
        "total_count -= min(increase_step, decrease_step)": "山頂被上坡與下坡各算了一次，扣掉較小的那份",
    },
    out="135/slopes",
)
