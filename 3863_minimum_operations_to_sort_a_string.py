class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        mx, mn = max(s), min(s)
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0
        if n == 2:
            return -1
        if s[0] == mn or s[-1] == mx:
            return 1
        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2
        return 3

sol = Solution()
print(sol.minOperations("edc"))