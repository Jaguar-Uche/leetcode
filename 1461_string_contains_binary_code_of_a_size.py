def generate_subcodes(num:int):
    g = num
    num = int("1"* num, 2)
    while num >= 0:
        yield bin(num)[2:].zfill(g)
        num -=1
def create_set(n):
    arr ={x for x in generate_subcodes(n)}
    return arr
# print(create_set(4))

def generate_substrings_of_len_k(s:str, k:int):
    seen = set()
    all_subcodes = create_set(k)
    for i in range(len(s)-k+1):
        sub = s[i:i+k]
        if sub in all_subcodes:
            seen.add(sub)
    print(all_subcodes)
    print(seen)
    return len(seen) == len(all_subcodes)

# print(generate_substrings_of_len_k("00110110", 2))

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        for i in range(len(s) - k + 1):
            seen.add(s[i:i + k])
            if len(seen) == 1 << k:
                return True
        return False

solution = Solution()
print(solution.hasAllCodes("01101", 1))

