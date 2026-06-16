class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for letter in s:
            match letter:
                case '*':
                    if len(result) > 0:
                        del result[-1]
                case '#':
                    if len(result) > 0:
                        result.extend(result)
                case '%':
                    result.reverse()
                case _:
                    result.append(letter)
        return "".join(result)

solution = Solution()
print(solution.processStr("ztv#*l"))