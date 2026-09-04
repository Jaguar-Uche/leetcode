# First create an array for max elements before we get to that element, na keep the minimum element from the back, up to that element

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_el = [0] * n
        min_el = [0] * n
        max_el[0] = nums[0]
        min_el[n-1] = nums[n-1]
        instability_score = float('inf')
        curr_index = -1
        for i in range(n):
            if i > 0:
                if max_el[i-1] > nums[i]:
                    max_el[i] = max_el[i-1]
                else:
                    max_el[i] = nums[i]
                if nums[n-i-1] < min_el[n-i]:
                    min_el[n-i-1] = nums[n-i-1]
                else:
                    min_el[n-i-1] = min_el[n-i]
        for i in range(n):
            diff = max_el[i] - min_el[i]
            if diff <= k and diff < instability_score:
                if instability_score == float('inf'):
                    curr_index = i
                instability_score = diff
        return curr_index

sol = Solution()
print(sol.firstStableIndex(nums = [6,1,4], k = 5))