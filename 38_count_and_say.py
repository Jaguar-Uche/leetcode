def count(s:str)->str:
    res =''
    prev_str = ''
    count = 0
    for c in s:
        if prev_str == '' or c == prev_str:
            count += 1
            prev_str = c
        else:
            res += str(count) + prev_str
            prev_str = c
            count = 1
    res += str(count) + prev_str
    return res
def count_string(n:int)->str:
    arr = ['0'] * n
    arr[0] = '1'
    for i in range(1, n):
        arr[i] =count(arr[i-1])
    return arr[n-1]

print(count_string(5))

# print(count("111222333445"))

class Solution:
    def countAndSay(self, n: int) -> str:
        return ""