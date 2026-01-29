from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        grid = []
        for i in range(numRows):
            grid.append([1 if j == 0 or j == i else 0 for j in range(i + 1)])
        if numRows > 2:
            for i in range(2, numRows):
                for j in range(1, i):
                    grid[i][j] = grid[i - 1][j - 1] + grid[i - 1][j]
        return grid
s = Solution()
print(s.generate(5))