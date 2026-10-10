class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        left, right = 0, max(diffs)

        while left < right:
            mid = (left + right) // 2

            # Operations required to make every difference <= mid
            needed = sum(max(0, d - mid) for d in diffs)

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        # Reduce every difference to at most the optimal threshold.
        for i, d in enumerate(diffs):
            k -= max(0, d - left)
            diffs[i] = min(d, left)

        # Use leftover operations to reduce some threshold values by 1.
        for i, d in enumerate(diffs):
            if k == 0:
                break
            if d == left:
                diffs[i] -= 1
                k -= 1

        return sum(d * d for d in diffs)