class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        steps = 0
        while num != 1:
            if num % 2 == 0:
                num //= 2
                steps += 1
            else:
                num = (num + 1) // 2
                steps +=2
        return steps

class Soln:
    def numSteps(self, s: str) -> int:
        steps = carry = 0
        for i in reversed(range(1, len(s))):
            val = int(s[i]) + carry
            if val % 2 == 0:
                steps += 1
            else:
                steps += 2
                carry = 1
        return steps + carry
solution = Soln()
print(solution.numSteps('11'))