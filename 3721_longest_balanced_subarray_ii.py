from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        seen_even = set()
        seen_odd = set()
        first = {0: -1}
        diff = 0
        ans = 0

        for i, x in enumerate(nums):
            if x % 2 == 0:
                if x not in seen_even:
                    seen_even.add(x)
                    diff += 1
            else:
                if x not in seen_odd:
                    seen_odd.add(x)
                    diff -= 1

            if diff in first and len(seen_odd) !=0 and len(seen_even)!=0:
                ans = max(ans, i - first[diff])
            else:
                first[diff] = i

        return ans


solution = Solution()
print(solution.longestBalanced([22,36,22]))
