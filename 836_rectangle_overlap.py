from typing import List
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x11, y11, x12, y12 = rec1
        x21, y21, x22, y22 = rec2
        # if any of the x falls within the other x, and the corresponding y of that x falls within the range, then yes it overlaps
        x_overlap = not (x12 <= x21 or x22 <= x11)
        y_overlap = not (y11 >= y22 or y21 >= y12)

        return x_overlap and y_overlap

sol = Solution()
print(sol.isRectangleOverlap(rec1 = [0,0,1,1], rec2 = [2,2,3,3]))