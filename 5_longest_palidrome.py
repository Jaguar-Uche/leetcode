def longestPalindrome(s: str) -> str:
    dictionary = {}
    for i, x in enumerate(s):
        dictionary.setdefault(x, []).append(i)
    current_length = 0
    palindrome_string = ""
    for letter in dictionary:
        if len(dictionary[letter]) > 1:
            for i, x in enumerate(dictionary[letter]):
                t = i
                while t + 1 < len(dictionary[letter]):
                    focus_string = s[x: dictionary[letter][t + 1] + 1]
                    if focus_string == focus_string[::-1] and len(focus_string) > current_length:
                        current_length = len(focus_string)
                        palindrome_string = focus_string
                    t += 1
        elif len(dictionary[letter]) == 1 and 1 > current_length:
            current_length = 1
            palindrome_string = letter
    return palindrome_string


def lengthOfLongestSubstring(s: str):
    seen = {}  # map char -> last index seen
    left = 0  # left pointer of sliding window
    best = 0
    palindrome_string = ""
    palindrome_length = 0

    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            # move left pointer to avoid duplicate
            check_string = s[seen[ch]:right+1]
            if check_string == check_string[::-1] and len(check_string) > palindrome_length:
                palindrome_string = check_string
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)

    return palindrome_string or s[0]

print(lengthOfLongestSubstring("bakoc"))