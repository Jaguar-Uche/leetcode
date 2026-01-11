def ClimbStairs(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n < 4:
        return n
    steps =[1,2]
    total = 0
    for step in steps:
        total += ClimbStairs(n - step, memo)
    memo[n] = total
    return total

print(ClimbStairs(7))