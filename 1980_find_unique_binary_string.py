from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)
        for i in range(2 ** n):
            x = f"{i:0{n}b}"
            if x not in nums:
                return x
solution = Solution()
print(solution.findDifferentBinaryString(["111","011","001"]))