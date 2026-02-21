from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums) - 2
        min_difference = float('inf')
        highest_seen = 0
        nums.sort()
        for i in range(n):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                diff = abs(total - target)
                if diff < min_difference:
                    min_difference = diff
                    highest_seen = total
                if total < target:
                    left += 1
                elif total == target:
                    return target
                else:
                    right -= 1
        return highest_seen

solution = Solution()
print(solution.threeSumClosest([0,0,0], 1))

