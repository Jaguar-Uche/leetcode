from typing import List
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique = set()
        even_and_zero=[]
        n = len(digits)
        for i in range(n):
            if digits[i] % 2 == 0:
                even_and_zero.append(i)
        for j in even_and_zero:
            prod = 1
            val = digits[j]
            for i in range(n):
                digit = digits[i]
                digit *=10
                digit += val
                if i != j:
                    for k in range(n):
                        if k != j  and k != i:
                            num = digits[k]
                            num *= 100
                            num += digit
                            if num >= 100:
                                unique.add(num)
        print(unique)
        return len(unique)

sol = Solution()
print(sol.totalNumbers([0,2,2]))