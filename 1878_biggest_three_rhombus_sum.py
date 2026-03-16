class Solution:
    def getBiggestThree(self, grid):
        rows, cols = len(grid), len(grid[0])
        sums = set()

        for r in range(rows):
            for c in range(cols):

                # size 0 rhombus
                sums.add(grid[r][c])

                k = 1
                while True:
                    if r-k < 0 or r+k >= rows or c-k < 0 or c+k >= cols:
                        break

                    total = 0

                    # top -> right
                    i, j = r-k, c
                    for step in range(k):
                        total += grid[i+step][j+step]

                    # right -> bottom
                    i, j = r, c+k
                    for step in range(k):
                        total += grid[i+step][j-step]

                    # bottom -> left
                    i, j = r+k, c
                    for step in range(k):
                        total += grid[i-step][j-step]

                    # left -> top
                    i, j = r, c-k
                    for step in range(k):
                        total += grid[i-step][j+step]

                    sums.add(total)
                    k += 1

        return sorted(sums, reverse=True)[:3]