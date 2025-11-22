def lengthOfLongestSubstring(s: str) -> int:
    seen = {}  # map char -> last index seen
    left = 0  # left pointer of sliding window
    best = 0

    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            # move left pointer to avoid duplicate
            left = seen[ch] + 1

        seen[ch] = right
        best = max(best, right - left + 1)

    return best


print(lengthOfLongestSubstring("abcdeefghaaakliljuoejaonleome"))