import unittest

from implement_12 import Solution


def roman_by_table(num: int) -> str:
    """獨立對照表，用來核對位數解法。"""
    table = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    parts = []
    for value, symbol in table:
        count, num = divmod(num, value)
        parts.append(symbol * count)
    return "".join(parts)


class IntToRomanTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_leetcode_examples(self):
        self.assertEqual(self.sol.intToRoman(3749), "MMMDCCXLIX")
        self.assertEqual(self.sol.intToRoman(58), "LVIII")
        self.assertEqual(self.sol.intToRoman(1994), "MCMXCIV")

    def test_ones_digit_rules(self):
        cases = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
        }
        for num, expected in cases.items():
            with self.subTest(num=num):
                self.assertEqual(self.sol.intToRoman(num), expected)

    def test_tens_digit_rules(self):
        cases = {
            10: "X",
            20: "XX",
            30: "XXX",
            40: "XL",
            50: "L",
            60: "LX",
            70: "LXX",
            80: "LXXX",
            90: "XC",
        }
        for num, expected in cases.items():
            with self.subTest(num=num):
                self.assertEqual(self.sol.intToRoman(num), expected)

    def test_hundreds_digit_rules(self):
        cases = {
            100: "C",
            200: "CC",
            300: "CCC",
            400: "CD",
            500: "D",
            600: "DC",
            700: "DCC",
            800: "DCCC",
            900: "CM",
        }
        for num, expected in cases.items():
            with self.subTest(num=num):
                self.assertEqual(self.sol.intToRoman(num), expected)

    def test_thousands(self):
        self.assertEqual(self.sol.intToRoman(1000), "M")
        self.assertEqual(self.sol.intToRoman(2000), "MM")
        self.assertEqual(self.sol.intToRoman(3000), "MMM")

    def test_bounds(self):
        self.assertEqual(self.sol.intToRoman(1), "I")
        self.assertEqual(self.sol.intToRoman(3999), "MMMCMXCIX")

    def test_mixed_places(self):
        cases = {
            128: "CXXVIII",
            949: "CMXLIX",
            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM",
            44: "XLIV",
            99: "XCIX",
            444: "CDXLIV",
            999: "CMXCIX",
            3888: "MMMDCCCLXXXVIII",
        }
        for num, expected in cases.items():
            with self.subTest(num=num):
                self.assertEqual(self.sol.intToRoman(num), expected)

    def test_all_valid_inputs_against_table(self):
        for num in range(1, 4000):
            self.assertEqual(
                self.sol.intToRoman(num),
                roman_by_table(num),
                msg=f"mismatch at {num}",
            )


if __name__ == "__main__":
    unittest.main()
