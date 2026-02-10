from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        step_count = 0
        current_jump_limit = 0
        farthest_index = 0
        for i in range(0, len(nums) - 1):
            farthest_index = max(farthest_index, i + nums[i])
            if i == current_jump_limit:
                step_count += 1
                current_jump_limit = farthest_index
        return step_count


solution = Solution()
test = [2,3,1,1,4]
print(solution.jump(test))

test = [2,3,0,0,4]
print(solution.jump(test))