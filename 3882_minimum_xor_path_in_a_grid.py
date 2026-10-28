class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # dp[j] stores all possible XOR values reaching column j
        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = {grid[i][j]}
                    continue

                # Possible XOR values from above and from the left
                prev = set()

                if i > 0:
                    prev.update(dp[j])      # From above

                if j > 0:
                    prev.update(dp[j - 1])  # From the left

                # Include the current cell in every path
                dp[j] = {x ^ grid[i][j] for x in prev}

        return min(dp[-1])
