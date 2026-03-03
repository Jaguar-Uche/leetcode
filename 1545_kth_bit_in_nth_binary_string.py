class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"

        mid = 1 << (n - 1)  # 2^(n-1)

        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            mirror = (1 << n) - k
            bit = self.findKthBit(n - 1, mirror)
            return "0" if bit == "1" else "1"