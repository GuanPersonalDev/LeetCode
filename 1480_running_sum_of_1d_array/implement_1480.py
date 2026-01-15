from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        result = [nums[0]]
        for i in nums[1:]:
            result.append(result[-1] + i)
        return result
solution = Solution()

test = [1,2,3,4]
print(solution.runningSum(test))