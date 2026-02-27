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
        carry = 0
        for i in range(len(s)-1, -1, -1 ):
            pass
solution = Soln()
print(solution.numSteps('11'))