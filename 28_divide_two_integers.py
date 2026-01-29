class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def check_result(input):
            if input < -2147483648:
                return -2147483648
            elif input > 2147483647:
                return 2147483647
            else:
                return input
        is_negative = False
        if dividend == 0:
            return 0
        elif divisor == 1:
            return check_result(dividend)
        elif divisor == -1:
            return check_result(-dividend)
        if dividend < 0 and divisor < 0:
            is_negative = False
            dividend = -dividend
            divisor = -divisor
        elif dividend > 0 and divisor <0:
            is_negative = True
            divisor = -divisor
        elif dividend < 0 and divisor > 0:
            is_negative = True
            dividend = -dividend
        result = 0
        while dividend >= divisor:
            dividend -= divisor
            result += 1
        if is_negative:
            result = -result
        return check_result(result)
s = Solution()
print(s.divide(-22,-3))