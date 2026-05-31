import time
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# first_time = time.time()
# print(fib(35))
# end_time = time.time()
# print(end_time - first_time)

# print()
# print()
memo = {1:1, 2:1}
def memoize_fib(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib(n)
        return memo[n]
#
# start_time = time.time()
# print(memoize_fib(35))
# end_time = time.time()
# print(end_time - start_time)
#
# print()
# print()

def bottom_up_fib(n):
    if n <= 2:
        return 1
    arr = [0]*(n+1)
    arr[1] = 1
    arr[2] = 1
    for i in range(3, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]

start_time = time.time()
print(bottom_up_fib(100))
end_time = time.time()
print()
print(end_time - start_time)



