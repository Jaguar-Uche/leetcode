class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        total = 0
        sorted_nums = sorted(nums)
        n = len(nums)
        for i in range(1, n + 1):
            if n % i != 0:
                continue
            for start in range(0, n, i):
                stop = start + i
                original = " ".join(map(str, nums[start:stop]))
                doubled = " ".join(map(str, sorted_nums[start:stop] * 2))
                if doubled.find(original) == -1:
                    break
            else:
                total += i

        return total
sol = Solution()
print(sol.sortableIntegers([7]))