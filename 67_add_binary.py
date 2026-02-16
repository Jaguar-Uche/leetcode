def addBinary(a: str, b: str) -> str:
    result = ""
    remainda = 0
    diff = len(a) - len(b)
    if diff > 0:
        b = ("0" * diff) + b
    else:
        a = ("0"* abs(diff)) + a
    for x in range(len(a)-1, -1, -1):
        addition = int(a[x]) + int(b[x]) + remainda
        if addition >=2:
            remainda = 1
        else:
            remainda = 0
        result = str(addition % 2) + result
    if remainda ==1:
        result = '1' + result
    return result
print(addBinary(a = "1010", b = "1011"))