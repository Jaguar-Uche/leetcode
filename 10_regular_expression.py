def isMatch(s, p):
    if '*' not in p:
        if len(s) != len(p):
            return False
        for i in range(len(s)):
            if s[i] == p[i] or p[i] == '.':
                continue
            else:
                return False
        return True
    else:

        return False
def check_asteriks(p, ind):
    pass

print(isMatch("ab", ".*"))