from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        num = nums[0]
        for i in nums:
            if counter == 0:
                num = i
            counter += 1 if num == i else -1
        return num

test = [3,2,3]
solution = Solution()
print(solution.majorityElement(test))

