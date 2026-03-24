from typing import List
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        MOD = 12345
        res = [[1] * n for _ in range(m)]
        # Forward pass (prefix)
        prefix = 1
        for i in range(m):
            for j in range(n):
                res[i][j] = prefix
                prefix = (prefix * grid[i][j]) % MOD

        # Backward pass (suffix)
        suffix = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                res[i][j] = (res[i][j] * suffix) % MOD
                suffix = (suffix * grid[i][j]) % MOD

        return res

solution = Solution()
print(solution.constructProductMatrix([[12345],[2],[1]]))

