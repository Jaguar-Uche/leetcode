from typing import List
class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0 for _ in range(n-k+1)] for _ in range(m-k+1)]
        if k == 1:
            return ans
        for i in range(m):
            use_height = i + k - 1
            if use_height >= m:
                break
            for j in range(n):
                use_width = j + k - 1
                if use_width < n:
                    arr = [x for row in grid[i:use_height + 1] for x in row[j:use_width + 1]]
                    # print_array(arr)
                    ans[i][j] = get_answer(arr)
                else:
                    break

        return ans

def get_answer(grid:List[int])-> int:
    grid.sort()
    differences = None
    for i in range(1, len(grid)):
        x = abs(grid[i] - grid[i-1])
        if x == 0:
            continue
        if differences is None or x < differences:
            differences = x
    if differences is None:
        return 0
    return differences
def print_array(grid):
    for row in grid:
        print(' '.join(map(str, row)))
    print()

solution = Solution()
print(solution.minAbsDiff([[1,-2,3],[2,3,5]], k = 2))

# get_sliding_array([[1,2,3],[4,5,6],[7,8,9]], 1)
# b = [[1,2,3],[4,5,6],[7,8,9]]
# print_array(b)
#
# a = [row[0:2] for row in b[0:2]]
# print(a)
