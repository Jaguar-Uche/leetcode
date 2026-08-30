from typing import List
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        left, right, n = 0, 0, len(nums)
        check_map = {'total':0}
        global_total = 0
        prev_xor = nums[0]
        while right < n:
            pass
        global_total = max(check_map['total'], global_total)
        return global_total