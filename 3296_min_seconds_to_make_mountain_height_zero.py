from typing import List
from math import sqrt
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def can(T):
            total = 0
            for t in workerTimes:
                k = int((sqrt(1 + 8 * T / t) - 1) // 2)
                total += k
                if total >= mountainHeight:
                    return True
            return False

        left, right = 0, 10 ** 18

        while left < right:
            mid = (left + right) // 2
            if can(mid):
                right = mid
            else:
                left = mid + 1

        return left


solution = Solution()
print(solution.minNumberOfSeconds(10, [3,2,2,4]))