from typing import List
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        dp = [[set()] for _ in range(n+1)]
        # dp[0].append(set())
        for i in range(n):
            # dp[i+1].append(set())
            for counts in dp[i]:
                new_count = counts
                new_count.add(nums[i])
                total += (len(new_count) ** 2)
                dp[i + 1].append(new_count)
        return total
sol = Solution()
print(sol.sumCounts([1,2,1]))