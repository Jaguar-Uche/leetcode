class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s

        mismatch1 = 0  # vs 010101...
        mismatch2 = 0  # vs 101010...

        ans = float('inf')

        left = 0

        for right in range(len(s)):

            # expected characters for the patterns
            expected1 = '0' if right % 2 == 0 else '1'
            expected2 = '1' if right % 2 == 0 else '0'

            if s[right] != expected1:
                mismatch1 += 1
            if s[right] != expected2:
                mismatch2 += 1

            # maintain window size n
            if right - left + 1 > n:

                expected1 = '0' if left % 2 == 0 else '1'
                expected2 = '1' if left % 2 == 0 else '0'

                if s[left] != expected1:
                    mismatch1 -= 1
                if s[left] != expected2:
                    mismatch2 -= 1

                left += 1

            # evaluate rotation
            if right - left + 1 == n:
                ans = min(ans, mismatch1, mismatch2)

        return ans

solution = Solution()
print(solution.minFlips('100100'))