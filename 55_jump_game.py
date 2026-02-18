from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        arr = [False]*n
        arr[0] = True
        for i in range(n):
            if arr[i]:
                for j in range(1, nums[i]+1):
                    arr[i+j] = True
                    if arr[n-1]:
                        return True
        return False

solution = Solution()
print(solution.canJump(nums=[2,3,1,1,4]))
class Stn:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)

        return True


