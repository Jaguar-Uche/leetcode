from typing import List
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x: int) -> int:
            total = 0
            while x:
                total += x % 10
                x //= 10
            return total

        n = len(nums)

        # Target order: digit sum first, then numeric value.
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        # Map each number to its target index.
        target = {num: i for i, num in enumerate(sorted_nums)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            j = i
            cycle_size = 0

            while not visited[j]:
                visited[j] = True
                cycle_size += 1
                j = target[nums[j]]

            swaps += max(0, cycle_size - 1)

        return swaps
sol = Solution()
print(sol.minSwaps([1,22,31]))