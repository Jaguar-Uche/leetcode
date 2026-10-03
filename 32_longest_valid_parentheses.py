class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len

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