from typing import List
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10

        for d in digits:
            freq[d] += 1

        ans = 0

        # Choose the units digit
        for units in range(0, 10, 2):
            if freq[units] == 0:
                continue

            # Use one occurrence of units
            freq[units] -= 1

            # Choose the hundreds digit
            for hundreds in range(1, 10):
                if freq[hundreds] == 0:
                    continue

                freq[hundreds] -= 1

                # Choose the tens digit
                for tens in range(10):
                    if freq[tens] > 0:
                        ans += 1

                freq[hundreds] += 1

            # Put units digit back
            freq[units] += 1

        return ans

sol = Solution()
print(sol.totalNumbers([0,2,2]))