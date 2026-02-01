from typing import List
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        total = nums[0]
        previous_least = 51
        current_least = 51
        for i in range(1, len(nums)):
            numb = nums[i]
            if numb < current_least:
                previous_least = current_least
                current_least = numb
            elif nums[i] < previous_least:
                previous_least = numb
        total += (previous_least + current_least)
        return total