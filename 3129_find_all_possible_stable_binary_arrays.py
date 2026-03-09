class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        dp = [[[[0] * (limit + 1) for _ in range(2)] for _ in range(one + 1)] for _ in range(zero + 1)]
        dp[1][0][0][1] = 1
        dp[0][1][1][1] = 1

        for z in range(zero + 1):
            for o in range(one + 1):
                for last in range(2):
                    for run in range(1, limit + 1):
                        count = dp[z][o][last][run]
                        if count == 0:
                            continue

                        if last == 0:
                            if run < limit and z + 1 <= zero:
                                dp[z + 1][o][0][run + 1] += count
                            if o + 1 <= one:
                                dp[z][o + 1][1][1] += count

                        else:
                            if run < limit and o + 1 <= one:
                                dp[z][o + 1][1][run + 1] += count
                            if z + 1 <= zero:
                                dp[z + 1][o][0][1] += count
        ans = 0
        for last in range(2):
            for run in range(1, limit + 1):
                ans += dp[zero][one][last][run]
        return ans % 1000000007

def solution_two(zero, one, limit):
    MOD = 10 ** 9 + 7

    dp = [[[0] * 2 for _ in range(one + 1)] for _ in range(zero + 1)]

    for z in range(1, min(zero, limit) + 1):
        dp[z][0][0] = 1

    for o in range(1, min(one, limit) + 1):
        dp[0][o][1] = 1

    for z in range(zero + 1):
        for o in range(one + 1):

            for k in range(1, limit + 1):
                if z - k >= 0:
                    dp[z][o][0] = (dp[z][o][0] + dp[z - k][o][1]) % MOD

                if o - k >= 0:
                    dp[z][o][1] = (dp[z][o][1] + dp[z][o - k][0]) % MOD
    return (dp[zero][one][0] + dp[zero][one][1]) % MOD

def solution_three(zero, one, limit):
    mod = 10 ** 9 + 7
    L = limit + 1

    dp0_prev, dp1_prev = [0] * (one + 1), [0] * (one + 1)
    for j in range(1, min(one, limit) + 1):
        dp1_prev[j] = 1

    dp1q = deque([dp1_prev[:]])  # dp1 rows, keep last L rows
    for i in range(1, zero + 1):
        dp0, dp1 = [0] * (one + 1), [0] * (one + 1)
        if i <= limit:
            dp0[0] = 1

        old1 = dp1q[0] if i >= L else None
        for j in range(1, one + 1):
            dp0[j] = (dp0_prev[j] + dp1_prev[j] - (old1[j] if old1 is not None else 0)) % mod
            dp1[j] = (dp0[j - 1] + dp1[j - 1] - (dp0[j - L] if j >= L else 0)) % mod

        dp1q.append(dp1[:])
        if len(dp1q) > L:
            dp1q.popleft()

        dp0_prev, dp1_prev = dp0, dp1

    return (dp0_prev[one] + dp1_prev[one]) % mod
solution = Solution()
print(solution.numberOfStableArrays(3,3,2))
print(solution.numberOfStableArrays(3,3,2))
