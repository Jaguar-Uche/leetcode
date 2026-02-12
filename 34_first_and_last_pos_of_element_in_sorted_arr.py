from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        midpoint = len(nums) // 2
        if nums[midpoint] > target:
            return self.searchRange(nums[:midpoint], target)
        if nums[midpoint] < target:
            return self.searchRange(nums[midpoint+1:], target)
        while nums[midpoint] == target:
            midpoint += 1
