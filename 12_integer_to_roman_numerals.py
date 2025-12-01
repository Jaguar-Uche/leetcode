memoi = {}
def intToRoman(num: int) -> str:
    roman_numeral = []
    first_divider = 10
    def convert_to_roman(number:int):
        if number in memoi.keys():
            return memoi[number]
        roman_num ={1:"I", 5:"V", 10:"X",50:"L", 100:"C", 500:"D", 1000:"M"}
        str_num = str(number)
        place_value = (10 ** (len(str_num) - 1))
        return_string =''
        if number in roman_num.keys():
            return_string = roman_num[number]
        else:
            if str_num[0] == "4":
                return_string = roman_num[1 * place_value] + roman_num[5 * place_value]
            elif str_num[0] == "9":
                return_string = roman_num[1 * place_value] + roman_num[10 * place_value]
            else:
                beacon = 5 * place_value
                if number < beacon:
                    return_string = roman_num[place_value] * (number // place_value)
                elif number > beacon:
                    check_val = (number - beacon)
                    return_string = roman_num[beacon] + (roman_num[place_value] * (check_val // place_value))
        memoi[number] = return_string
        return return_string
    if num <= first_divider:
        return convert_to_roman(num)
    while num > first_divider:
        if num % first_divider == 0:
            first_divider *= 10
            continue
        roman_numeral.append(convert_to_roman(num % first_divider))
        num -= (num % first_divider)
        first_divider *= 10
    roman_numeral.append(convert_to_roman(num))
    return "".join(reversed(roman_numeral))


class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]

        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]

        roman = []

        for v, s in zip(values, symbols):
            while num >= v:
                num -= v
                roman.append(s)

        return "".join(roman)


print(intToRoman(58))
print(intToRoman(1994))
print(intToRoman(3999))