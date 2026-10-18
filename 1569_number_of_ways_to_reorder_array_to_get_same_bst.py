class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute combinations C[i][j].
        comb = [[0] * n for _ in range(n)]
        for i in range(n):
            comb[i][0] = 1
            for j in range(1, i + 1):
                comb[i][j] = (
                    comb[i - 1][j - 1] + comb[i - 1][j]
                ) % MOD

        def dfs(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            l, r = len(left), len(right)

            ways_left = dfs(left)
            ways_right = dfs(right)

            # Interleave left and right subtree elements.
            interleavings = comb[l + r][l]

            return (
                interleavings * ways_left % MOD
                * ways_right % MOD
            ) % MOD

        return (dfs(nums) - 1) % MOD
