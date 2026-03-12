class Solution:
    def __init__(self):
        self._roman_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        self._value_list = [1, 5, 10, 50, 100, 500, 1000]

    def romanToInt(self, s: str) -> int:
        i = 0
        l = len(s)
        total = 0
        while i < l:
            value, i = self.getValue(s, i)
            total += value
        return total

    def getValue(self, s: str, i: int) -> tuple[int, int]:
        roman = s[i]
        value_index = self._roman_list.index(roman)
        value = self._value_list[value_index]
        next_index = i+1
        enable_suffix = value == 1 or value == 10 or value == 100
        if next_index >= len(s) or not enable_suffix:
            return value, next_index
        next_roman = s[next_index]
        next_value_index = self._roman_list.index(next_roman)
        index_offset = next_value_index - value_index
        if 0 < index_offset < 3:
            next_value = self._value_list[next_value_index]
            value = next_value - value
            next_index = i+2
        return value, next_index


solution = Solution()
test = "III"
print(solution.romanToInt(test))

test = "LVIII"
print(solution.romanToInt(test))

test = "MCMXCIV"
print(solution.romanToInt(test))