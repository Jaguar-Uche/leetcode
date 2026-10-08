class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opening_brackets = []
        result = ""
        for idx, char in enumerate(s):
            if char == "(":
                if len(opening_brackets) > 0:
                    result += "("
                opening_brackets.append(idx)
            elif char == ")":
                opening_brackets.pop()
                if len(opening_brackets) > 0:
                    result += ")"
        return result

sol = Solution()
print(sol.removeOuterParentheses(s = "()()"))