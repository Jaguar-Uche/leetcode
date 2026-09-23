class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x

        if target < 0:
            return -1

        if target == 0:
            return n

        left = 0
        curr_sum = 0
        longest = -1

        for right in range(n):
            curr_sum += nums[right]

            while curr_sum > target and left <= right:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == target:
                longest = max(longest, right - left + 1)

        if longest == -1:
            return -1

        return n - longest