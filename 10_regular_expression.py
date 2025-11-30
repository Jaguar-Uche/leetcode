def isMatch(s, p):
    is_match = False
    indices_of_dot = []
    indices_of_asteriks = []
    indices_of_first = []
    patterns = []
    for i in range(len(p)):
        if p[i] == '.':
            if len(p) - i >= len(s):
                patterns.append(p[i::])
            indices_of_dot.append(i)
        elif p[i] == '*':
            if len(p) - i >= len(s):
                patterns.append(p[i::])
            indices_of_asteriks.append(i)
        elif p[i] == s[0]:
            if len(p) - i >= len(s):
                patterns.append(p[i::])
            indices_of_first.append(i)




print(isMatch("ab", ".*"))