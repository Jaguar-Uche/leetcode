class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        result = 1

        while n > 0:
            if n % 2 == 1:  # if current bit is 1
                result *= x
            x *= x  # square base
            n //= 2  # shift bits right

        return result


class secondSolution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        result = 1

        while n > 0:
            if n % 2 == 1:  # if current bit is 1
                result *= x
            x *= x  # square base
            n //= 2  # shift bits right

        return result
