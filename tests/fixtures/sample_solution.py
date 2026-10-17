from typing import List


class Solution:
    def total(self, nums: List[int]) -> int:
        acc = 0
        for i in range(len(nums)):
            acc += nums[i]
        return acc


class Store:
    def __init__(self):
        self.items = []

    def add(self, value: int) -> None:
        self.items.append(value)


print("module-level output should be swallowed")
