from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        output_arr = []
        s = set()
        for i in range(len(arr) - 1):
            diff = abs(arr[i+1] - arr[i])
            min_diff = min(min_diff, diff)

sol = Solution()
print(sol.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))