from functools import lru_cache

def numbers_with_sum(n, s):
    if n <= 0 or s < 1 or s > 9 * n:
        return []

    @lru_cache(maxsize=None)
    def possible(pos, remaining):
        # Can the remaining digits produce this sum?
        digits_left = n - pos

        if remaining < (1 if pos == 0 else 0):
            return False

        if remaining > 9 * digits_left:
            return False

        if pos == n:
            return remaining == 0

        start = 1 if pos == 0 else 0

        for digit in range(start, 10):
            if digit > remaining:
                break

            if possible(pos + 1, remaining - digit):
                return True

        return False

    result = []

    def backtrack(pos, remaining, path):
        if pos == n:
            result.append(path)
            return

        start = 1 if pos == 0 else 0

        for digit in range(start, 10):
            if digit > remaining:
                break

            next_remaining = remaining - digit

            # Skip branches that cannot produce a solution.
            if not possible(pos + 1, next_remaining):
                continue

            backtrack(pos + 1, next_remaining, path + str(digit))

    backtrack(0, s, "")
    return result

def sum_of_squares(n):
    n = str(n)
    total = 0
    for char in n:
        total += int(char) ** 2
    return total

class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res = numbers_with_sum(num, sum)
        max_sum_of_squares = 0
        number_with_max = ""
        for number in res:
            if sum_of_squares(number) >= max_sum_of_squares:
                max_sum_of_squares = sum_of_squares(number)
                number_with_max = number
        return  number_with_max

sol = Solution()
print(sol.maxSumOfSquares(2, 3))

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        min_val = int("1" + ("0" * (num-1)))
        max_val = int("9" * num)
        max_sum_of_squares = 0
        no_with_max = ""
        for number in range(max_val, min_val-1, -1):
            if sum_of_digits(number) == sum:
                if sum_of_squares(number) > max_sum_of_squares:
                    max_sum_of_squares = sum_of_squares(number)
                    no_with_max = str(number)
        return no_with_max

sol = Solution()
print(sol.maxSumOfSquares(2, 3))