def is_sublist(nums, arr):
    if not nums:
        return True
    s = " ".join(map(str, arr))
    if s.find(" ".join(map(str, nums))) != -1:
        return True
    return False
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        total = 0
        sorted_nums = sorted(nums)
        n = len(nums)
        for i in range(1,n+1):
            if n % i == 0:
                for d in range(0, n, i):
                    start, stop = d, d+i
                    double_arr = sorted_nums[start:stop] * 2
                    if not is_sublist(nums[start:stop], double_arr):
                        break
                else:
                    total += i
        return total
sol = Solution()
print(sol.sortableIntegers([7]))