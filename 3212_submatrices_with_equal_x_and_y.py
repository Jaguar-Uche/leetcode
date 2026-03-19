from typing import List
class Solution:
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])
        check = [(0, 0)] * n
        res = 0

        for i in range(m):
            x = y = 0
            for j in range(n):
                if grid[i][j] == 'X':
                    x += 1
                elif grid[i][j] == 'Y':
                    y += 1

                a, b = check[j]
                a += x
                b += y
                check[j] = (a, b)

                if a == b and a != 0:
                    res += 1

        return res
solution = Solution()
print(solution.numberOfSubmatrices([["X","Y","."],["Y",".","."]]))