from typing import List

# 3 ways to delete, remove the 2 from the front or the 2 from the back or delete the shortest from front, and the shortest from the back from the back

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        max_number = max(nums)
        min_number = min(nums)
        index_of_max = nums.index(max_number)
        index_of_min = nums.index(min_number)
        min_way = float('inf')
        min_way = min((max(index_of_min, index_of_max))+1, min_way)
        min_way = min(n-min(index_of_min, index_of_max),min_way)
        min_way = min((min(index_of_min, index_of_max)+1 + n- max(index_of_min,index_of_max)) , min_way)
        return min_way

sol = Solution()
print(sol.minimumDeletions([101]))