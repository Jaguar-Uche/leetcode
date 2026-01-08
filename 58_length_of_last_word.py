def lengthOfLastWord(s: str) -> int:
    count = 0
    for i in range(len(s)-1, -1, -1):
        if count == 0 and s[i] == ' ':
            continue
        elif s[i] == ' ':
            break
        else:
            count += 1

    return count
