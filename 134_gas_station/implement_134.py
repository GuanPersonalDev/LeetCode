from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        start_index = 0
        tank = 0
        for i in range(0, len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start_index = i+1
                tank = 0
        return start_index

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

test_gas = [3, 1, 1]
test_cost = [1, 2, 2]
print(solution.canCompleteCircuit(test_gas, test_cost))