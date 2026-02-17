from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        change_rows = set()
        change_cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    change_rows.add(i)
                    change_cols.add(j)
        if len(change_rows) != 0 or len(change_cols) != 0:
            for i in change_rows:
                matrix[i] = [0] * len(matrix[i])
            for j in change_cols:
                t = 0
                while t < len(matrix):
                    matrix[t][j] = 0
                    t +=1
        print(matrix)


solution = Solution()
solution.setZeroes(matrix=[[1,1,1],[1,0,1],[1,1,1]])