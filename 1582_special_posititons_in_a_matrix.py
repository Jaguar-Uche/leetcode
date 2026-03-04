from typing import List
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        row_sums = [0] * m
        col_sums = [0] * n
        res = 0
        for i in range(m):
            for j in range(n):
                row_sums[i] += mat[i][j]
                col_sums[j] += mat[i][j]

        for i in range(m):
            if row_sums[i] == 1:
                for j in range(n):
                    if mat[i][j] == 1:
                        if col_sums[j] == 1:
                            res += 1
                        break
        return res

solution = Solution()
print(solution.numSpecial([[0,0,1,0],[0,0,0,0],[0,0,0,0],[0,1,0,0]]))
# grid = [[0 for _ in range(2)] for _ in range(2)]
# print(grid)