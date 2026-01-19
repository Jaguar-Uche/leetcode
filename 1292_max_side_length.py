from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # Build prefix sum matrix
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                ps[i][j] = (
                    mat[i-1][j-1]
                    + ps[i-1][j]
                    + ps[i][j-1]
                    - ps[i-1][j-1]
                )

        max_side = 0

        # Try all possible side lengths
        for k in range(1, min(m, n) + 1):
            found = False
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    total = (
                        ps[i+k][j+k]
                        - ps[i][j+k]
                        - ps[i+k][j]
                        + ps[i][j]
                    )
                    if total <= threshold:
                        found = True
                        break
                if found:
                    break

            if found:
                max_side = k
            else:
                break  # no larger square will work

        return max_side
