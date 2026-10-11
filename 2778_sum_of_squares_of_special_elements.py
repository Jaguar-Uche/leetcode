from typing import List
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for i in range(1, n+1):
            if n % i == 0:
                total += (nums[i-1] ** 2)
        return total

soln = Solution()
print(soln.sumOfSquares([2,7,1,19,18,3]))