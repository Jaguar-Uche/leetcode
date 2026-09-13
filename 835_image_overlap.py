from typing import List
# find 1s from img1, find 1s from img 2
# Then using the 1s from img1, find the displacement from the other one, and find the one that gives you max displacement
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1_arr = []
        img2_arr = []
        hash = {}
        n = len(img1)
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    img1_arr.append((i,j))
                if img2[i][j] == 1:
                    img2_arr.append((i,j))
        # print(img1_arr)
        # print(img2_arr)
        for (a,b) in img1_arr:
            for (c,d) in img2_arr:
                e,f = c-a, d-b
                hash[(e,f)] = hash.get((e,f), 0) + 1
        # print(hash)
        return max(hash.values())

sol = Solution()
print(sol.largestOverlap(img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]))