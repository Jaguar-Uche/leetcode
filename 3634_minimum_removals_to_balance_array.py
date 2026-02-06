from typing import List
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = n
        right = 0
        for left in range(n):
            while right < n and nums[right] <= nums[left] * k:
                right += 1
            ans = min(ans, n - (right - left))
        return ans


s = Solution()
print(s.minRemoval([2,12], 2))

# n= 5
# for i in range(n-1, -1, -1):
#     print(f"These are for i = {i}")
#     for j in range(i+1, n):
#         print(j)