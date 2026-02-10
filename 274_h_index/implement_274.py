from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counter_max_index = len(citations)
        counter = [0] * (counter_max_index+1)
        for c in citations:
            counter[min(c, counter_max_index)] += 1
        cited_count = 0
        for i in range(counter_max_index, -1, -1):
            cited_count += counter[i]
            if cited_count >= i:
                return i
        return 0


solution = Solution()
test = [3,0,6,1,5]
print(solution.hIndex(test))

test = [1,3,1]
print(solution.hIndex(test))
