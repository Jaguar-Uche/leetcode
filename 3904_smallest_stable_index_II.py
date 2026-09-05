class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix_max = nums[0]
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
        for i in range(n):
            prefix_max = max(prefix_max, nums[i])
            diff = prefix_max - suffix_min[i]
            if diff <= k:
                return i
        return -1