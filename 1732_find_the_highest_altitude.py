from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        for height in gain:
            altitudes.append(altitudes[-1] + height)
        return max(altitudes)

solution = Solution()
print(solution.largestAltitude([-4,-3,-2,-1,4,3,2]))
