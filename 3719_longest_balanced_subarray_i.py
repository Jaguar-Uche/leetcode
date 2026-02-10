from typing import List
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        for i in range(n):
            num_check = set()
            if nums[i] % 2 == 0:
                even_seen = 1
                odd_seen = 0
            else:
                odd_seen = 1
                even_seen = 0
            seen_before = 0
            num_check.add(nums[i])
            for j in range(i + 1, n):
                if nums[j] in num_check:
                    seen_before += 1
                    if even_seen == odd_seen:
                        max_len = max(max_len, (even_seen + odd_seen + seen_before))
                    continue
                num_check.add(nums[j])
                if nums[j] % 2 == 0:
                    even_seen += 1
                else:
                    odd_seen += 1
                if even_seen == odd_seen:
                    max_len = max(max_len, (even_seen + odd_seen + seen_before))

        return max_len

s = Solution()
print(s.longestBalanced([2, 4, 1, 3, 3, 3, 3]))