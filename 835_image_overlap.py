from typing import List
# find 1s from img1, find 1s from img 2
# Then using the 1s from img1, find the displacement from the other one, and find the one that gives you max displacement
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1_ones = []
        img2_ones = []
        shifts = {}

        n = len(img1)

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    img1_ones.append((i, j))

                if img2[i][j] == 1:
                    img2_ones.append((i, j))

        for r1, c1 in img1_ones:
            for r2, c2 in img2_ones:
                shift = (r2 - r1, c2 - c1)
                shifts[shift] = shifts.get(shift, 0) + 1

        return max(shifts.values(), default=0)

sol = Solution()
print(sol.largestOverlap(img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]))