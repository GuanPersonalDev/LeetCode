from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = len(prices)
        for i in range(1, l):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit

test = [7,1,5,3,6,4]
solution = Solution()
print(solution.maxProfit(test))

test = [1,2,3,4,5]
print(solution.maxProfit(test))
