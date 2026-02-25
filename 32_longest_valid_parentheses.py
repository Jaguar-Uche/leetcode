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

solution = Solution()
print(solution.longestValidParentheses("(()"))
print(solution.longestValidParentheses("()(()"))
print(solution.longestValidParentheses(")()())"))