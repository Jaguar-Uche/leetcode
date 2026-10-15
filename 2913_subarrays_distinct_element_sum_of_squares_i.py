from typing import List
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        # Find the subarrays, and use a set to keep track of distinct elements, and add squares
        n = len(nums)
        for i in range(n):
            for j in range(i+1):
                count = set()
                count.update(nums[j:i+1])
                total += (len(count) ** 2)
        return total

sol = Solution()
print(sol.sumCounts([1,1]))