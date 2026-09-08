class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        return (n - 1000) + 1

sol = Solution()
print(sol.countCommas(1000000))