from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)

        # First and last occurrence of every character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        # Find the smallest valid interval for each character
        for c in range(26):
            if last[c] == -1:
                continue

            left = first[c]
            right = last[c]

            i = left
            valid = True

            while i <= right:
                idx = ord(s[i]) - ord('a')

                # This character appeared before `left`,
                # so we cannot make a valid substring starting at `left`.
                if first[idx] < left:
                    valid = False
                    break

                # Its last occurrence extends our interval.
                right = max(right, last[idx])

                i += 1

            if valid:
                intervals.append((left, right))

        # Earliest finishing interval first
        intervals.sort(key=lambda x: x[1])

        ans = []
        end = -1

        for left, right in intervals:
            if left > end:
                ans.append(s[left:right + 1])
                end = right

        return ans