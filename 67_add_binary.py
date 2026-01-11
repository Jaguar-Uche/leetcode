def addBinary(a: str, b: str) -> str:
    result = ""
    remainda = 0
    if len(a) > len(b):
        b = "0"* (len(a)-len(b)) + b
    elif len(a) < len(b):
        a = "0"* (len(b)-len(a)) + a
    for x in range(len(a)-1, -1, -1):
        addition = int(a[x]) + int(b[x]) + remainda
        if addition == 2:
            remainda = 1
            result = "0" + result
        elif addition == 3:
            remainda = 1
            result = "1" + result
        else:
            remainda = 0
            result = str(addition) + result
    if remainda ==1:
        result = '1' + result
    return result

print(addBinary(a = "1010", b = "1011"))
