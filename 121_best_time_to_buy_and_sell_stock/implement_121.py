from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for p in prices:
            if p < min_price:
                min_price = p
                continue

            new_profit = p - min_price
            if new_profit > max_profit:
                max_profit = new_profit
        return max_profit




solution = Solution()
test =[7,1,5,3,6,4]
print(solution.maxProfit(test))

test = [7,6,4,3,1]
print(solution.maxProfit(test))
