from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # A valid parentheses string needs even length.
        if (m + n - 1) % 2 == 1:
            return False

        # Starting point must be '('
        if grid[0][0] == ')':
            return False

        # Ending point must be ')'
        if grid[m - 1][n - 1] == '(':
            return False

        # dp[i][j] = set of possible balances at this cell
        dp = [[set() for _ in range(n)] for _ in range(m)]

        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                if grid[i][j] == '(':
                    change = 1
                else:
                    change = -1

                # From above
                if i > 0:
                    for balance in dp[i - 1][j]:
                        new_balance = balance + change

                        if new_balance >= 0:
                            dp[i][j].add(new_balance)

                # From left
                if j > 0:
                    for balance in dp[i][j - 1]:
                        new_balance = balance + change

                        if new_balance >= 0:
                            dp[i][j].add(new_balance)

        return 0 in dp[m - 1][n - 1]