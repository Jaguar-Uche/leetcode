from typing import List
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total =0
        for i in range(len(points)-1):   
            current_x = points[i][0]
            current_y = points[i][1]
            next_x = points[i+1][0]
            next_y = points[i+1][1]
            while current_x != next_x or current_y != next_y:
                if current_x < next_x:
                    current_x +=1
                elif current_x > next_x:
                    current_x -=1
                if current_y < next_y:
                    current_y +=1
                elif current_y > next_y:
                    current_y -=1
                total +=1
        return total
s = Solution()
print(s.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))