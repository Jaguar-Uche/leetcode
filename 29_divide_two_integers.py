def check_result(input):
    if input < -2147483648:
        return -2147483648
    elif input > 2147483647:
        return 2147483647
    else:
        return input
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = False
        if dividend < 0:
            is_negative = True
            dividend = -dividend
        if divisor < 0:
            is_negative = not is_negative
            divisor = -divisor
        res = dividend // divisor
        return check_result(res * -1 if is_negative else res)

class Soln:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0) != (divisor < 0)  # True if signs differ
        dividend = abs(dividend)
        divisor = abs(divisor)
        while True:
