from typing import List
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0

        def is_non_decreasing(arr):
            return all(arr[i] >= arr[i - 1] for i in range(1, len(arr)))

        while not is_non_decreasing(nums):
            min_sum = float("inf")
            min_idx = 0

            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    min_idx = i

            nums[min_idx] = min_sum
            nums.pop(min_idx + 1)
            operations += 1

        return operations


sol = Solution()
print(sol.minimumPairRemoval([2,2,-1,3,-2,2,1,1,1,0,-1]))