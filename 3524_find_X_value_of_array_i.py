from typing import List
import math
# return an array result, where result[i] is the number of ways to remove prefix and suffix from an array, so that the product of remainder % k == i
# The strategy is to remove different subarrays, and then divide by the number removed, and increment the value at the remainder of the division
# I start with removing an empty subarray at the front, then remove an empty subarray(suffix) at the back until I have one element left.
# Then continue removing elements(prefix) from the front in this manner, until i have one element left
# [a,b,c,d]
# In essence, just go from [] in the front, and [] at back, then [d], [c,d], [b,c,d]
# Then remove [a] at the front, and repeat same until the end
# This is the computation. I will calculate the product of the array, then for everything i remove, i will divide the product by it, and then check the remainder, and increment, result at the remainder
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Extend every previous subarray
            for r in range(k):
                if dp[r]:
                    new_r = (r * num) % k
                    new_dp[new_r] += dp[r]

            # Start a new subarray with just num
            new_dp[num % k] += 1

            # Add today's subarrays to the final answer
            for r in range(k):
                result[r] += new_dp[r]

            dp = new_dp

        return result

sol = Solution()
print(sol.resultArray( nums = [1,1,2,1,1], k = 2))



