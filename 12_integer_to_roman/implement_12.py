
class Solution:
    def intToRoman(self, num: int) -> str:
        palces = [
            (1000, "M", "", ""),
            (100, "C", "D", "M"),
            (10, "X", "L", "C"),
            (1, "I", "V", "X"),
        ]
        result = ""
        for value, one, five, ten in palces:
            d = num // value
            num %= value
            if d == 9:
                result += one + ten
            elif d >= 5:
                result += five + one * (d-5)
            elif d == 4:
                result += one + five
            else:
                result += one * d
        return result
