from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remain_right = 0
        remain_left = 0
        start_index = -1
        for i in range(0, len(gas)):
            offset = gas[i] - cost[i]
            if offset >= 0:
                if start_index == -1:
                    start_index = i
            remain_right += offset
            if remain_right < 0:
                start_index = -1
                remain_left += remain_right
                remain_right = 0
        if remain_right + remain_left >= 0:
            return start_index
        return -1

solution = Solution()
test_gas = [1, 2, 3, 4, 5]
test_cost = [3, 4, 5, 1, 2]
print(solution.canCompleteCircuit(test_gas, test_cost))

test_gas = [2, 3, 4]
test_cost = [3, 4, 3]
print(solution.canCompleteCircuit(test_gas, test_cost))

test_gas = [5, 8, 2, 8]
test_cost = [6, 5, 6, 6]
print(solution.canCompleteCircuit(test_gas, test_cost))