import math
def sumFourDivisors(nums, memo ={}) -> int:
    total = 0
    for num in nums:
        if num in memo:
            total += memo[num]
            continue
        divisors = set()
        for divider in range(1, int(math.sqrt(num) + 1)):
            if num % divider == 0:
                divisors.add(divider)
                divisors.add(num // divider)
        if len(divisors) == 4:
            sum_total = sum(divisors)
            memo[num] = sum_total
            total += sum_total

    return total

print(sumFourDivisors([21,4,7]))
print(sumFourDivisors([21,21]))
print(sumFourDivisors([1,2,3,4,5]))