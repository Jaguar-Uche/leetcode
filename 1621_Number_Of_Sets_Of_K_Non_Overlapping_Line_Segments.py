from functools import lru_cache

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        @lru_cache(None)
        def dp(start, remaining):
            if remaining == 0:
                return 1

            if start >= n - 1:
                return 0

            total = 0

            # Choose the start of the next segment
            for left in range(start, n - 1):

                # Choose the end of that segment
                for right in range(left + 1, n):
                    total += dp(right, remaining - 1)
                    total %= MOD

            return total

        return dp(0, k)
sol = Solution()
print(sol.numberOfSets(4,2))