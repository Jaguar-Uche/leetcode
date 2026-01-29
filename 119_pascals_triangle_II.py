from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        grid = []
        for i in range(rowIndex+1):
            grid.append([1 if j == 0 or j == i else 0 for j in range(i + 1)])
        if rowIndex >= 2:
            for i in range(2, rowIndex+1):
                for j in range(1, i):
                    grid[i][j] = grid[i - 1][j - 1] + grid[i - 1][j]
        return grid[rowIndex]

s = Solution()
print(s.getRow(2))