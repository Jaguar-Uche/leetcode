def isIsomorphic(s: str, t: str) -> bool:
    letter_map = {}
    for i in range(len(s)):
        if s[i] in letter_map:
            if letter_map[s[i]] != t[i]:
                return False
        else:
            if t[i] in letter_map.values():
                return False
            letter_map[s[i]] = t[i]
    return True