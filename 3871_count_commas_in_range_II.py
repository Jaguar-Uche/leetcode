class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        if n >= 1000000000000000:
            total += (((n - 1000000000000000 ) + 1) * 5)
            n = 999999999999999
        if n >= 1000000000000:
            total += (((n - 1000000000000) + 1) * 4)
            n = 999999999999
        if n >= 1000000000:
            total += (((n - 1000000000) + 1) * 3)
            n = 999999999
        if n >= 1000000:
            total += (((n - 1000000) + 1) * 2)
            n = 999999
        if n >= 1000:
            total += (((n -1000)+1) *1)
        return total

sol = Solution()
print(sol.countCommas(1000000000000000))