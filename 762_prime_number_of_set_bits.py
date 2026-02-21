primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 31}
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        total = 0
        for i in range(left, right+1):
            if i.bit_count() in primes:
                total += 1
        return total

solution = Solution()
print(solution.countPrimeSetBits(6,10))