def isValid(self, s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    open=[]
    closed = []
    square = []
    hash_table = {}
    for index,char in enumerate(s):
        if char == '(':
            open.append(index)
            hash_table[index] = True
        elif char == ')':
            if len(open)>0:
                i = open.pop(-1)
                hash_table[i] = False
                if (index - i + 1) % 2 != 0:
                    return False
                cases = s[i:index + 1]
                for t in range(len(cases)):
                    case = t + i
                    if case in hash_table.keys() and hash_table[case] == True:
                        return False
            else:
                return False
        elif char == '[':
            square.append(index)
            hash_table[index] = True
        elif char == ']':
            if len(square)>0:
                i = square.pop(-1)
                hash_table[i] = False
                if (index - i + 1) % 2 != 0:
                    return False
                else:
                    cases = s[i:index + 1]
                    for t in range(len(cases)):
                        case = t + i
                        if case in hash_table.keys() and hash_table[case] == True:
                            return False
            else:
                return False
        elif char == '{':
            closed.append(index)
            hash_table[index] = True
        elif char == '}':
            if len(closed)>0:
                i = closed.pop(-1)
                hash_table[i] = False
                if (index - i + 1) % 2 != 0:
                    return False
                else:
                    cases = s[i:index + 1]
                    for t in range(len(cases)):
                        case = t+i
                        if case in hash_table.keys() and hash_table[case] == True:
                            return False
            else:
                return False
    if True in hash_table.values():
        return False
    else:
        return True