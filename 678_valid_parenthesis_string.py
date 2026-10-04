class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for char in s:
            if char == '(':
                low += 1
                high += 1

            elif char == ')':
                low -= 1
                high -= 1

            else:  # '*'
                low -= 1       # treat * as ')'
                high += 1      # treat * as '('

            # We can never have a negative minimum balance.
            low = max(low, 0)

            # Even the maximum possible balance is negative.
            # Therefore no interpretation can work.
            if high < 0:
                return False

        return low == 0