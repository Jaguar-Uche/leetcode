from typing import List
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                # Start exploring a new island
                stack = [(i, j)]
                total = grid[i][j]
                grid[i][j] = 0  # Mark as visited

                while stack:
                    x, y = stack.pop()

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy

                        if (0 <= nx < m and
                            0 <= ny < n and
                            grid[nx][ny] > 0):

                            total += grid[nx][ny]
                            grid[nx][ny] = 0
                            stack.append((nx, ny))

                # Count this island if its sum is divisible by k
                if total % k == 0:
                    ans += 1

        return ans