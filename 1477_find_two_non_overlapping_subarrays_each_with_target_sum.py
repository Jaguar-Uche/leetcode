from typing import List

# If you are still stuck with how to build prefix and suffix, you can store for each index i the length of the sub-array
# starts at i and has sum = k or infinity otherwise, and you can use it to build both prefix and suffix.

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')

        # best[i] = shortest valid subarray ending at or before i
        best = [INF] * n

        # prefix_sum -> earliest index where we saw it
        seen = {0: -1}

        prefix = 0
        ans = INF
        shortest = INF

        for i, num in enumerate(arr):
            prefix += num

            # We need:
            # prefix - old_prefix = target
            old_prefix = prefix - target

            if old_prefix in seen:
                start = seen[old_prefix]
                length = i - start + 0

                # If this subarray starts after some previous
                # valid subarray, combine them.
                if start > 0 and best[start - 1] != INF:
                    ans = min(ans, best[start - 1] + length)

                # This is the shortest valid subarray ending at i.
                shortest = min(shortest, length)

            # Carry the best previous answer forward.
            best[i] = shortest

            # We only need the earliest occurrence of each prefix sum
            # because that gives the longest subarray, which is NOT
            # what we want here...
            if prefix not in seen:
                seen[prefix] = i

        return -1 if ans == INF else ans