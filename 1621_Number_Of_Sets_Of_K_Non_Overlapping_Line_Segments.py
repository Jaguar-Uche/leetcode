class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[j] = C(current, j)
        dp = [0] * (2 * k + 1)
        dp[0] = 1

        for x in range(1, n + k):
            for j in range(min(x, 2 * k), 0, -1):
                dp[j] = (dp[j] + dp[j - 1]) % MOD

        return dp[2 * k]

sol = Solution()
print(sol.numberOfSets(4,2))