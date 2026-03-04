from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        total_count = l
        i = 1
        while i < l:
            if ratings[i] == ratings[i-1]:
                i += 1
                continue
            increase_step = 0
            while i < l and ratings[i] > ratings[i-1]:
                increase_step += 1
                total_count += increase_step
                i += 1
            if i == l :
                return total_count
            decrease_step = 0
            while i < l and ratings[i] < ratings[i-1]:
                decrease_step += 1
                total_count += decrease_step
                i += 1
            # double counted at peak
            total_count -= min(increase_step, decrease_step)
        return total_count



solution = Solution()
test = [1, 0, 2]
print(solution.candy(test))

test = [1, 2, 2]
print(solution.candy(test))