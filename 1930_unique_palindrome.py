def countPalindromicSubsequence(s: str) -> int:
    first = {}
    last = {}

    # record first and last occurrences
    for i, ch in enumerate(s):
        if ch not in first:
            first[ch] = i
        last[ch] = i

    ans = 0

    # for each character as the outer character of the palindrome
    for ch in first:
        if last[ch] - first[ch] >= 2:  # must have space between
             # collect distinct chars between first and last occurrence
            middle = set(s[first[ch] + 1: last[ch]])
            if len(middle) > ans:
                ans = len(middle)

    return ans

print(countPalindromicSubsequence("abababa"))