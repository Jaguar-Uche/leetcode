class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        global_total = 0
        stack = []
        for index, char in enumerate(s):
            if char == '(':
                stack.append([index,0])
            else:
                total = 0
                [idx, content] = stack.pop()
                if content > 0:
                    total += content * 2
                else:
                    total = 1
                if not stack:
                    global_total += total
                else:
                    stack[-1][1] += total
        return global_total
sol = Solution()
print(sol.scoreOfParentheses("(()(()))"))
