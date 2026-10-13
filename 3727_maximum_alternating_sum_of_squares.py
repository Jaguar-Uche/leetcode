from typing import List
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = [ x ** 2 for x in nums]
        squares.sort()
        n = len(squares)
        num_negative = (n)//2
        negative_sum = sum(squares[:num_negative])
        positive_sum = sum(squares[num_negative:])

        return positive_sum - negative_sum

soln = Solution()
print(soln.maxAlternatingSum([1,2,3]))