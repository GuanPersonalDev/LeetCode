from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        left_product, right_product = 1, 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
        for i in range(n-1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer

solution = Solution()

test = [1, 2, 3, 4]
print(solution.productExceptSelf(test))