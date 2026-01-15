def isHappy(n: int, s = set()):
    if n in s:
        return False
    string_n = str(n)
    number =0
    for letter in string_n:
        number += pow((int(letter)), 2)
    if number == 1:
        return True
    else:
        s.add(n)
        return isHappy(number, s)