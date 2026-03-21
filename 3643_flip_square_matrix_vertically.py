from typing import List
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(y, y+k):
            left = x
            right = x + k -1
            while left < right:
                grid[left][i], grid[right][i] = grid[right][i], grid[left][i]
                left += 1
                right -= 1
            pass
        return grid

solution = Solution()
print(solution.reverseSubmatrix(grid = [[3,4,2,3],[2,3,4,2]], x = 0, y = 2, k = 2))