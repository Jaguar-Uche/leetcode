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
        count = 0
        temp_dividend = 0
        ans = 0
        while True:
            if dividend < divisor:
                break
            elif dividend == divisor:
                ans += 1
                break
            res = divisor << count
            # print(f"The divisor{divisor} << count{count} is {res}")
            if res > dividend:

                dividend -= temp_dividend
                # print(f"dividend becomes {dividend}")
                # print(f"{2 ** (count -1)} is added to ans {ans}")
                ans += (2 ** (count -1))
                count = 0
            elif res < dividend:
                temp_dividend = res
                count +=1
            else:
                ans += (2 ** (count))
                break

        if is_negative:
            ans  = -ans
        return ans

solt = Soln()
print(solt.divide(40,3))

class Gpt:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        # Overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign of result
        negative = (dividend > 0) != (divisor > 0)

        # Convert both to negative (safer range)
        dividend = -abs(dividend)
        divisor = -abs(divisor)

        ans = 0

        # Main loop: subtract largest doubled divisor each time
        while dividend <= divisor:
            value = divisor
            multiple = 1

            # Double until it would go past dividend
            while value >= INT_MIN // 2 and dividend <= value + value:
                value += value
                multiple += multiple

            dividend -= value
            ans += multiple

        return -ans if negative else ans

sol = Gpt()
print(sol.divide(40,3))
