def plusOne(digits):
    single_number = int("".join(map(str, digits)))
    single_number += 1
    digits = [int(x) for x in str(single_number)]
    return digits

arr = [1,2,3,4,5]
print(int("".join(map(str, arr))))