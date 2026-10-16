from typing import List
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        total = [0] * (4 * n)
        squares = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, left, right, delta):
            length = right - left + 1
            d = delta

            squares[node] = (
                squares[node]
                + 2 * d * total[node]
                + length * d * d
            ) % MOD

            total[node] = (
                total[node] + length * d
            ) % MOD

            lazy[node] = (lazy[node] + d) % MOD

        def push(node, left, right):
            if lazy[node] == 0 or left == right:
                return

            mid = (left + right) // 2
            d = lazy[node]

            apply(node * 2, left, mid, d)
            apply(node * 2 + 1, mid + 1, right, d)

            lazy[node] = 0

        def update(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                apply(node, left, right, 1)
                return

            push(node, left, right)
            mid = (left + right) // 2

            if ql <= mid:
                update(node * 2, left, mid, ql, qr)

            if qr > mid:
                update(node * 2 + 1, mid + 1, right, ql, qr)

            total[node] = (
                total[node * 2] + total[node * 2 + 1]
            ) % MOD

            squares[node] = (
                squares[node * 2] + squares[node * 2 + 1]
            ) % MOD

        last_seen = {}
        answer = 0

        for i, x in enumerate(nums):
            prev = last_seen.get(x, -1)

            # Increase distinct counts for subarrays
            # starting in [prev + 1, i].
            update(1, 0, n - 1, prev + 1, i)

            # Root stores the sum of squares for all
            # subarrays ending at index i.
            answer = (answer + squares[1]) % MOD

            last_seen[x] = i

        return answer

sol = Solution()
print(sol.sumCounts([1,2,3]))