from typing import List
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        pairs = set()
        nums.sort()
        mid_point = len(nums) // 2
        highest = len(nums) - 1
        for i in range(mid_point):
            pairs.add(nums[i] + nums[highest - i])
        return max(pairs)
sol = Solution()
print(sol.minPairSum([3,5,4,2,4,6]))