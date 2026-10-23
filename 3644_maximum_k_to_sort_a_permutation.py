from typing import List
class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = -1

        for i, x in enumerate(nums):
            if i != x:
                ans &= x

        return max(ans, 0)

sol = Solution()
print(sol.sortPermutation([3,2,1,0]))