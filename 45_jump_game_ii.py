from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [None] * n
        arr[0] = 0
        for i in range(n):
            print("This is the first arr")
            print(arr)
            print("operations started")
            if arr[i] is not None:
                for j in range(1, nums[i] + 1):
                    if i + j < n:
                        if arr[i+j] is None:
                            arr[i+j] = arr[i] + 1
                    print(arr)

                    if arr[n - 1] is not None:
                        return arr[n-1]


class Soltn:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps


solution = Solution()
sol = Soltn()
print(sol.jump([2,3,1,1,4]))
# print(solution.jump(nums=[2,1,1,1,1]))