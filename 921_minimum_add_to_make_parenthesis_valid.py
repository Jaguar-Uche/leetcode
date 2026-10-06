class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening_bracket =[]
        closing_bracket = []

        for index, char in enumerate(s):
            if char == '(':
                opening_bracket.append(index)
            else:
                if len(opening_bracket) > 0:
                    opening_bracket.pop()
                else:
                    closing_bracket.append(index)

        return len(opening_bracket) + len(closing_bracket)

sol = Solution()
print(sol.minAddToMakeValid("((("))