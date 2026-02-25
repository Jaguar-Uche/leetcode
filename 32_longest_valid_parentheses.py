class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_valid = 0
        n = len(s)

        # ---- Left to Right ----
        open_count = 0
        close_count = 0

        for i in range(n):
            if s[i] == '(':
                open_count += 1
            else:
                close_count += 1

            if open_count == close_count:
                max_valid = max(max_valid, 2 * close_count)
            elif close_count > open_count:
                open_count = 0
                close_count = 0

        # ---- Right to Left ----
        open_count = 0
        close_count = 0

        for i in range(n - 1, -1, -1):
            if s[i] == '(':
                open_count += 1
            else:
                close_count += 1

            if open_count == close_count:
                max_valid = max(max_valid, 2 * open_count)
            elif open_count > close_count:
                open_count = 0
                close_count = 0

        return max_valid

class Soln:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        max_len = 0

        for i in range(1, n):
            if s[i] == ')':
                # Case 1: "()"
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2

                # Case 2: "...))"
                else:
                    prev_len = dp[i-1]
                    j = i - prev_len - 1
                    if j >= 0 and s[j] == '(':
                        dp[i] = dp[i-1] + 2
                        if j - 1 >= 0:
                            dp[i] += dp[j-1]

                max_len = max(max_len, dp[i])

        return max_len

solution = Soln()
print(solution.longestValidParentheses("(()"))
print(solution.longestValidParentheses("()(()"))
print(solution.longestValidParentheses(")()())"))