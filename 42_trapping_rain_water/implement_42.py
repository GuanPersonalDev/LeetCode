from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left_index = 0
        right_index = len(height) - 1
        left_max = height[left_index]
        right_max = height[right_index]

        while left_index < right_index:
            if left_max < right_max:
                left_index += 1
                left_max = max(left_max, height[left_index])
                total += left_max - height[left_index]
            else:
                right_index -= 1
                right_max = max(right_max, height[right_index])
                total += right_max - height[right_index]
        return total

solution = Solution()
test = [0,1,0,2,1,0,1,3,2,1,2,1]
print(solution.trap(test))
