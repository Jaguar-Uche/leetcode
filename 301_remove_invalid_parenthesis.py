class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        open_remove = 0
        close_remove = 0

        for char in s:
            if char == '(':
                open_remove += 1

            elif char == ')':
                if open_remove > 0:
                    open_remove -= 1
                else:
                    close_remove += 1

        result = set()

        def backtrack(index, path, balance, open_remove, close_remove):
            if index == len(s):
                if balance == 0 and open_remove == 0 and close_remove == 0:
                    result.add("".join(path))
                return

            char = s[index]

            # Normal character
            if char not in "()":
                path.append(char)

                backtrack(index + 1,path,balance,open_remove,close_remove)

                path.pop()

            # '('
            elif char == '(':
                # Option 1: remove it
                if open_remove > 0:
                    backtrack(index + 1,path,balance,open_remove - 1,close_remove)

                # Option 2: keep it
                path.append('(')

                backtrack(index + 1,path,balance + 1,open_remove,close_remove)

                path.pop()

            # ')'
            else:

                # Option 1: remove it
                if close_remove > 0:
                    backtrack(index + 1,path,balance,open_remove,close_remove - 1)

                # Option 2: keep it
                # Can't keep ')' if there is no '(' available
                if balance > 0:
                    path.append(')')

                    backtrack(index + 1,path,balance - 1,open_remove,close_remove)

                    path.pop()

        backtrack(0, [], 0, open_remove, close_remove)

        return list(result)


sol = Solution()
print(sol.removeInvalidParentheses("(a)())()"))