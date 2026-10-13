from typing import List
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        result = 0
        squares = [x ** 2 for x in nums]
        squares.sort(reverse=True)
        left, right = 0, len(squares)-1
        while left <= right:
            if left == right:
                result += squares[left]
            result += squares[left]
            left += 1
            result -= squares[right]
            right -= 1

        return result

soln = Solution()
print(soln.maxAlternatingSum([1,2,3]))