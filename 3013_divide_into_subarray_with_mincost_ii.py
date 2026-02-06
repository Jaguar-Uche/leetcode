import sys
from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: list[int], k: int, dist: int) -> int:
        # Window Size (positions for k-1 starting points)
        window_size = dist + 1

        # Initial window (positions 1..dist+1)
        # Compute sum and maintain sorted lists
        windowSum = sum(nums[i] for i in range(1, min(len(nums), window_size + 1)))
        selected = SortedList(nums[i] for i in range(1, min(len(nums), window_size + 1)))
        candidates = SortedList()

        def balance():
            """Ensure selected has exactly k-1 smallest elements."""
            nonlocal windowSum
            # If we must pick more
            while len(selected) < k - 1:
                val = candidates.pop(0)
                selected.add(val)
                windowSum += val
            # If too many, move largest selected to candidates
            while len(selected) > (k - 1):
                val = selected.pop(-1)
                candidates.add(val)
                windowSum -= val

        # Balance the first window
        balance()
        minSum = windowSum

        # Slide the window across the array
        for i in range(window_size + 1, len(nums)):
            out_val = nums[i - window_size]
            # Remove out-of-window value
            if out_val in selected:
                selected.remove(out_val)
                windowSum -= out_val
            else:
                candidates.remove(out_val)

            # Add new value
            new_val = nums[i]
            if selected and new_val < selected[-1]:
                selected.add(new_val)
                windowSum += new_val
            else:
                candidates.add(new_val)

            # Balance and update minimum
            balance()
            minSum = min(minSum, windowSum)

        return nums[0] + minSum

s = Solution()
print(s.minimumCost([1, 2, 3, 4, 5], 2, 4))