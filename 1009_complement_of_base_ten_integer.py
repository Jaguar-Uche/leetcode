class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        b = int("1" * n.bit_length(), 2)
        return n ^ b

class Solution_Two:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        res = 0
        pos = 0
        while n:
            bit = n & 1
            if bit == 0:
                res |= (1 << pos)
            pos += 1
            n >>= 1
        return res
solution = Solution_Two()
print(solution.bitwiseComplement(10))




