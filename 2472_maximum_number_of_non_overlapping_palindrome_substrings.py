class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        total = 0
        last_end = -1

        for j in range(n):
            for i in range(j + 1):

                # This palindrome would overlap the previous one
                if i <= last_end:
                    continue

                left = i
                right = j

                while left <= right:
                    if s[left] == s[right]:
                        left += 1
                        right -= 1
                    else:
                        break

                if left > right and (j - i + 1) >= k:
                    total += 1
                    last_end = j

                    # We already chose the earliest possible ending position
                    break

        return total

sol = Solution()
print(sol.maxPalindromes("fttfjofpnpfydwdwdnns", 2))