from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        current_index = m+n-1
        nums1_progress = m-1
        nums2_progress = n-1
        while current_index >= 0:
            if nums1_progress < 0:
                nums1[current_index] = nums2[nums2_progress]
                nums2_progress -= 1
            elif nums2_progress < 0:
                nums1[current_index] = nums1[nums1_progress]
                nums1_progress -= 1
            else:
                a = nums1[nums1_progress] if nums1_progress > -1 else 0
                b = nums2[nums2_progress] if nums2_progress > -1 else 0
                if a > b:
                    nums1[current_index] = a
                    nums1_progress -= 1
                else:
                    nums1[current_index] = b
                    nums2_progress -= 1
            current_index -= 1

nums1 = [-1,0,0,3,3,3,0,0,0]
nums2 = [1,2,2]

solution = Solution()
solution.merge(nums1, 6, nums2, 3)

for i in nums1:
    print(i)