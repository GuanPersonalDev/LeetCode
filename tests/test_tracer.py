import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from leetviz import TraceError, tracer

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "sample_solution.py"


class TraceSolutionTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        patcher = mock.patch.object(tracer, "OUTPUT_DIR", Path(self.tmp.name))
        patcher.start()
        self.addCleanup(patcher.stop)
        self.addCleanup(self.tmp.cleanup)

    def trace(self, **kwargs):
        params = dict(source=str(FIXTURE), method="Solution.total", cases={"c": {"nums": [1, 2, 3]}}, out="t/sample")
        params.update(kwargs)
        path = tracer.trace_solution(**params)
        return json.loads(path.read_text(encoding="utf-8"))

    def test_records_result_and_final_locals(self):
        case = self.trace()["cases"]["c"]
        self.assertEqual(case["result"], 6)
        self.assertEqual(case["steps"][-1]["return"], 6)
        self.assertEqual(case["steps"][-1]["vars"]["acc"], 6)

    def test_records_each_loop_iteration(self):
        steps = self.trace()["cases"]["c"]["steps"]
        acc_line = next(i for i, line in enumerate(FIXTURE.read_text().splitlines(), 1) if "acc += nums[i]" in line)
        self.assertEqual(sum(1 for s in steps if s["line"] == acc_line), 3)

    def test_snapshot_is_not_mutated_by_later_steps(self):
        data = self.trace(method="Store.add", cases={"c": {"value": 5}})
        steps = data["cases"]["c"]["steps"]
        self.assertEqual(steps[0]["vars"]["self.items"], [])
        self.assertEqual(steps[-1]["vars"]["self.items"], [5])

    def test_input_is_not_mutated(self):
        nums = [1, 2, 3]
        data = self.trace(cases={"c": {"nums": nums}})
        self.assertEqual(data["cases"]["c"]["input"], {"nums": [1, 2, 3]})

    def test_notes_attach_by_source_text(self):
        steps = self.trace(notes={"acc += nums[i]": "累加"})["cases"]["c"]["steps"]
        self.assertEqual(sum(1 for s in steps if s.get("note") == "累加"), 3)

    def test_unknown_note_raises(self):
        with self.assertRaises(TraceError):
            self.trace(notes={"no such line": "x"})

    def test_step_limit_raises(self):
        with mock.patch.object(tracer, "MAX_STEPS", 3):
            with self.assertRaises(TraceError):
                self.trace()

    def test_range_covers_method(self):
        data = self.trace()
        first, last = data["range"]
        self.assertIn("def total", data["code"][first - 1])
        self.assertIn("return acc", data["code"][last - 1])


if __name__ == "__main__":
    unittest.main()
