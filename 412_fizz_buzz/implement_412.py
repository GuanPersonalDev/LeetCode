from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            str = ""
            if i % 3 == 0:
                str += "Fizz"
            if i % 5 == 0:
                str += "Buzz"
            if str == "":
                str = f'{i}'
            result.append(str)
        return result

solution = Solution()
print(solution.fizzBuzz(15))