class Solution:
    def reverseDegree(self, s: str) -> int:
        n = len(s)
        total = 0
        for i in range(n):
            total += ((i+1) * (26 - (ord(s[i]) - ord('a'))))
        return total