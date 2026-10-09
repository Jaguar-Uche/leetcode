class Solution:
    def minInsertions(self, s: str) -> int:
        result = 0
        need = 0

        for char in s:
            if char == '(':
                need += 2

                if need % 2 == 1:
                    result += 1
                    need -= 1

            else:
                need -= 1

                if need == -1:
                    result += 1
                    need = 1

        return result + need


sol = Solution()
print(sol.minInsertions("))))))((()))(()(()))"))