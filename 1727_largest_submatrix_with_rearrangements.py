from typing import List
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        heights = [0] * n
        max_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            sorted_row = sorted(heights, reverse=True)
            for width_index, height in enumerate(sorted_row):
                area = height * (width_index + 1)
                max_area = max(max_area, area)
        return max_area

solution = Solution()
print(solution.largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]]))

# matrix = [[1,1,1],[1,1,1],[1,1,1]]
# prefix = [[None] * len(matrix[0]) for _ in range(len(matrix))]
# print(prefix[0][1])
