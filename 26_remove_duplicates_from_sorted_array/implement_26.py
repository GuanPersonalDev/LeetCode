from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result_index = 0
        for i in range(0, len(nums)):
            if nums[result_index] != nums[i]:
                result_index += 1
                nums[result_index] = nums[i]
        return result_index + 1

test = [0,0,1,1,1,2,2,3,3,4]
solution = Solution()
print(solution.removeDuplicates(test))


