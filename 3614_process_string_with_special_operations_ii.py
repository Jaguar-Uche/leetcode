class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = []

        for ch in s:
            prev = lengths[-1] if lengths else 0

            if ch == '*':
                lengths.append(max(0, prev - 1))
            elif ch == '#':
                lengths.append(prev * 2)
            elif ch == '%':
                lengths.append(prev)
            else:
                lengths.append(prev + 1)

        if not lengths or k >= lengths[-1]:
            return "."

        for i in range(len(s) - 1, -1, -1):
            prev = lengths[i - 1] if i > 0 else 0

            if s[i] == '#':
                if prev > 0:
                    k %= prev

            elif s[i] == '%':
                k = prev - 1 - k

            elif s[i] == '*':
                # If length decreased from prev to prev-1,
                # the removed character cannot be the answer
                pass

            else:
                # This character was appended at index prev
                if k == prev:
                    return s[i]

        return "."

solution = Solution()
# print(solution.processStr("a#b%*", ))



