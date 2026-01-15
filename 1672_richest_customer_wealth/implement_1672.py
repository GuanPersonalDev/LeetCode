from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for moneys in accounts:
            sum = 0
            for v in moneys:
                sum += v
            if sum > max:
                max = sum
        return max


test = [[2,8,7],[7,1,3],[1,9,5]]

solution = Solution()
print(solution.maximumWealth(test))