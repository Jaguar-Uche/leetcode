from typing import List
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        rotate_90 = rotate_360 = rotate_270 = rotate_180 = True
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[i][j]:
                    rotate_360 = False
                if mat[i][j] != target[j][n - i- 1]:
                    rotate_90 = False
                if mat[i][j] != target[n - i - 1][n - j - 1]:
                    rotate_180 = False
                if mat[i][j] != target[n - j - 1][i]:
                    rotate_270 = False
        return rotate_90 or rotate_360 or rotate_270 or rotate_180
solution = Solution()
print(solution.findRotation(mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]))
