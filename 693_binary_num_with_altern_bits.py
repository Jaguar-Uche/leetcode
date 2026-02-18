class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev_bit = None
        while n !=0:
            current_bit = n & 1
            if prev_bit is None or prev_bit != current_bit:
                prev_bit = current_bit
            else:
                return False
            n >>= 1
        return True

solution = Solution()
print(solution.hasAlternatingBits(10))