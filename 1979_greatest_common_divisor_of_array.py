from typing import List
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_element = min(nums)
        max_element = max(nums)
        for i in range(min_element, 0, -1):
            if max_element % i == 0 and min_element % i == 0:
                return i
        return 1

solution = Solution()
print(solution.findGCD([3,3]))