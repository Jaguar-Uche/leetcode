def reverse(x):
    number_string = str(x)
    is_negative = False
    if number_string[0] == "-":
        is_negative = True
        number_string = number_string[1:]
    new_string = number_string[::-1]
    if int(new_string) > 2147483648 or int(new_string) < -2147483647:
        return 0
    new_number = int(new_string)
    if is_negative:
        return new_number * -1
    return new_number

print(reverse(-214748347))
print(reverse(214748348))
