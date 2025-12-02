def isMatch(s, p):
    is_match = False
    indices_of_dot = []
    indices_of_asteriks = []
    indices_of_first = []
    patterns = []
    special_patterns = []
    for i in range(len(p)):
        if p[i] == '.':
            if len(p) - i >= len(s):
                patterns.append(p[i::])
            indices_of_dot.append(i)
        elif p[i] == s[0]:
            if len(p) - i >= len(s):
                patterns.append(p[i::])
            indices_of_first.append(i)
        if s in patterns:
            return True
print(isMatch("ab", ".*"))