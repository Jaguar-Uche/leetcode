from typing import List
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        i = 1
        n = len(nums)
        if n == 3:
            return False
        while i <n-1 and  nums[i] > nums[i-1]:
            i += 1
        p = i= i-1
        if p == 0:
            return False
        while i < n-1 and nums[i+1] < nums[i]:
            i += 1
        q = i
        if q - p == 0:
            return False
        while i <= n -2 and nums[i+1] > nums[i]:
            i += 1
        r = i
        if r - q ==0 or r < n -1:
            return False
        if p != q != r:
            return True
        return False