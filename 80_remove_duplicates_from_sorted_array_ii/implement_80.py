from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current_index = 0
        for n in nums:
            if current_index < 2 or n > nums[current_index - 2]:
                nums[current_index] = n
                current_index += 1
        return current_index


test = [1,1,1,2,2,3]
solution = Solution()
print(solution.removeDuplicates(test))