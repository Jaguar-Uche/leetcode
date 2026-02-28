class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = 0
        bit_num = 0
        for i in range(1,n+1):
            if i & (i - 1) == 0:
                bit_num += 1
            result = ((result << bit_num) + i) % 1000000007
        return result

solution = Solution()
print(solution.concatenatedBinary(12))

