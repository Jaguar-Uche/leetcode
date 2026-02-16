class Solution:
    def reverseBits(self, n: int) -> int:
        # return int(bin(n)[2:].zfill(32)[::-1], 2)
        # Convert to binary, then remove the first two ie 0b and then fill with 0s until 32
        # then reverse string and convert to base 2
        res = 0

        for _ in range(32):
            bit = n & 1  # extract last bit
            res = (res << 1) | bit  # append it
            n >>= 1  # remove last bit

        return res


print(f"{10:032b}")
