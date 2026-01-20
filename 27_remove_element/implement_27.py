from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ori_len = len(nums)
        result_len = 0
        for i in range(0, ori_len):
            n = nums[i]
            if n != val:
                nums[result_len] = n
                result_len += 1
        return result_len

test = [3,2,2,3]
test_val = 3
solution = Solution()
result = solution.removeElement(test, test_val)
print(result)
print('array context')
for i in range(0, result):
    print(test[i])
