def sum_and_product_of_digits(n):
    n = abs(n)
    digit_sum = 0
    digit_product = 1 if n > 0 else 0  # 0 has a product of 0
    while n > 0:
        digit = n % 10
        digit_sum += digit
        digit_product *= digit
        n //= 10
    return digit_sum + digit_product


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        if n % sum_and_product_of_digits(n) == 0:
            return True
        return False