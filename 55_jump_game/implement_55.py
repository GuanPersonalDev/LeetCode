from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        s = 0
        for n in nums:
            if s < 0:
                return False
            if n > s:
                s = n
            s -= 1
        return True


test = [2,3,1,1,4]
solution = Solution()
print(solution.canJump(test))

test = [3,2,1,0,4]
print(solution.canJump(test))

test = [0]
print(solution.canJump(test))
test = [2,5,0,0]
print(solution.canJump(test))