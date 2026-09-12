from typing import List
from functools import lru_cache
from bisect import bisect_right
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:

        # Keep the original index.
        # [start, end, weight, original_index]
        jobs = [
            [start, end, weight, i]
            for i, (start, end, weight) in enumerate(intervals)
        ]

        # Sort by start time
        jobs.sort(key=lambda x: x[0])

        starts = [job[0] for job in jobs]
        n = len(jobs)

        # next_idx[i] = first interval whose start > jobs[i].end
        next_idx = [0] * n

        for i in range(n):
            next_idx[i] = bisect_right(starts, jobs[i][1])

        @lru_cache(None)
        def dp(i, k):
            """
            Returns:
                (maximum weight, lexicographically smallest list of
                 original indices)

            starting from interval i, with at most k intervals remaining.
            """

            if i == n or k == 0:
                return (0, ())

            # Option 1: skip this interval
            skip_weight, skip_indices = dp(i + 1, k)

            # Option 2: take this interval
            take_weight, take_indices = dp(next_idx[i], k - 1)

            take_weight += jobs[i][2]
            take_indices = (jobs[i][3],) + take_indices

            # Compare the two choices
            if take_weight > skip_weight:
                return (take_weight, tuple(sorted(take_indices)))

            if skip_weight > take_weight:
                return (skip_weight, skip_indices)

            # Same weight -> lexicographically smaller indices
            take_indices = tuple(sorted(take_indices))

            if take_indices < skip_indices:
                return (take_weight, take_indices)

            return (skip_weight, skip_indices)

        _, answer = dp(0, 4)

        return list(answer)