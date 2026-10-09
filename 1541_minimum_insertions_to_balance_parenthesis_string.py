class Solution:
    def minInsertions(self, s: str) -> int:
        opening = []
        seen = 0
        result = 0
        for index, char in enumerate(s):
            if char == '(':
                if seen == 0:
                    opening.append(index)
                    continue
                elif seen == 1:
                    if len(opening) > 0:
                        opening.pop()
                        result += 1
                    else:
                        result += 2
                elif seen == 2:
                    result += 1
                else:
                    if seen % 2 == 0:
                        result += (seen // 2)
                    else:
                        result += (seen // 2 + 2)
                seen = 0
                opening.append(index)
            else:
                if seen == 1:
                    if len(opening) > 0:
                        opening.pop()
                        seen = 0
                    else:
                        seen += 1
                else:
                    seen += 1
        if seen == 0:
            pass
        elif seen == 1:
            if len(opening) > 0:
                opening.pop()
                result += 1
            else:
                result += 2
        elif seen == 2:
            result += 1
        else:
            if seen % 2 == 0:
                result += (seen // 2)
            else:
                result += (seen // 2 + 2)
        result += (2 * len(opening))
        return result


sol = Solution()
print(sol.minInsertions("(()))"))