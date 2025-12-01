def romanToInt(s: str) -> int:
    roman_num = {"I":1, "V" :5,"X" : 10,"L" : 50, "C" : 100,"D": 500,"M":1000}
    number = 0
    for index, x in enumerate(s):
        if index+1 < len(s) and roman_num[s[index+1]] > roman_num[x]:
            number -= roman_num[x]
        else:
            number += roman_num[x]
    return number
print(romanToInt("IV"))
print(romanToInt("CXL"))