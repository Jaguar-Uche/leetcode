class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        seen_zero = False
        if n == 1:
            return True
        for i in range(1, n):
            if s[i] == '0':
                seen_zero = True
            if seen_zero and s[i] == '1':
                return False
        return True
solution = Solution()
print(solution.checkOnesSegment("1101"))