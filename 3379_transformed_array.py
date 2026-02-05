from typing import List
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result =[0]* n
        for i in range(n):
            if nums[i] == 0:
                ind = i
            else:
                ind = i + nums[i]
            if ind > (len(nums) - 1):
                ind = ind % len(nums)
            elif ind < -(len(nums) -1):
                ind = -(abs(ind) % len(nums))
            result[i] =nums[ind]
        return result

s = Solution()
print(s.constructTransformedArray([-1,4,-1]))