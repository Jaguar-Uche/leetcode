def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)

    # dp[i][j] = does s[0..i) match p[0..j)
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Empty string matches empty pattern
    dp[0][0] = True

    # Empty string can match pattern like "a*b*c*"
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]  # ignore the x* pair

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # Two choices:
                # 1. Ignore the x* → look at dp[i][j-2]
                # 2. Use x* at least once → if current char matches, stay at j
                no_use = dp[i][j - 2]
                use_once_or_more = dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.')
                dp[i][j] = no_use or use_once_or_more
            else:
                # Normal char or dot
                char_match = (s[i - 1] == p[j - 1]) or (p[j - 1] == '.')
                dp[i][j] = dp[i - 1][j - 1] and char_match

    return dp[m][n]

print(isMatch('ba', '.*'))