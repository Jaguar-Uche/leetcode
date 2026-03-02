from typing import List
def bubble_back(nums, start, end):
    while start > end:
        nums[start], nums[start-1] = nums[start-1], nums[start]
        start -= 1


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n  = len(grid)
        zeros = []
        min_swaps = 0
        for i in range(n):
            trail_zeros = 0
            for j in reversed(range(n)):
                if grid[i][j] == 0:
                    trail_zeros += 1
                else:
                    break
            zeros.append(trail_zeros)
        for k in range(n):
            required = n - k - 1
            if zeros[k] >= required:
                continue
            else:
                for l in range(k+1, n):
                    if zeros[l] >= required:
                        bubble_back(zeros, l, k)
                        min_swaps += (l-k)
                        break
                else:
                    return -1
        return min_swaps

solution = Solution()
print(solution.minSwaps([[1,0,0],[1,1,0],[1,1,1]]))