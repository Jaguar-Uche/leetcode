from typing import List
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        dp1 = [None] * len(nums)
        dp2 = [None] * len(nums)
        dp3 = [None] * len(nums)
        max_seen = float('-inf')
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if dp1[i-1] is None:
                    dp1[i] =  nums[i] + nums[i - 1]
                else:
                    dp1[i] = max(dp1[i-1] + nums[i],  nums[i] + nums[i - 1])
                if dp2[i-1] is not None and dp3[i-1] is not None:
                    dp3[i] = max(dp2[i-1] + nums[i], dp3[i-1] + nums[i])
                elif dp2[i-1] is not None:
                    dp3[i] = dp2[i-1] + nums[i]
                elif dp3[i-1] is not None:
                    dp3[i] = dp3[i-1] + nums[i]
                if dp3[i] is not None:
                    max_seen = max(max_seen, dp3[i])
            elif nums[i] < nums[i - 1]:
                if dp1[i-1] is not None and dp2[i-1] is not None:
                    dp2[i] = max(dp1[i-1] + nums[i], dp2[i-1] + nums[i])
                elif dp1[i-1] is not None:
                    dp2[i] = dp1[i-1] + nums[i]
                elif dp2[i-1] is not None:
                    dp2[i] = dp2[i-1] + nums[i]
        print(nums)
        print(dp1)
        print(dp2)
        print(dp3)
        return max_seen
