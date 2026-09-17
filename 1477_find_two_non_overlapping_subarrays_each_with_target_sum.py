from typing import List

# If you are still stuck with how to build prefix and suffix, you can store for each index i the length of the sub-array
# starts at i and has sum = k or infinity otherwise, and you can use it to build both prefix and suffix.

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')

        # best[i] = shortest target-sum subarray
        # completely inside arr[:i]
        best = [INF] * (n + 1)

        prefix = 0
        seen = {0: -1}
        ans = INF

        for i in range(n):
            prefix += arr[i]

            # Don't use a subarray ending at i.
            best[i + 1] = best[i]

            if prefix - target in seen:
                start = seen[prefix - target]
                length = i - start

                # Previous subarray must lie completely before `start`.
                if best[start + 1] != INF:
                    ans = min(ans, best[start + 1] + length)

                best[i + 1] = min(best[i + 1], length)

            if prefix not in seen:
                seen[prefix] = i

        return -1 if ans == INF else ans