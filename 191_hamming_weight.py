def hammingWeight(n: int) -> int:
    set_bit = 0
    while n > 0:
        if n % 2 != 0:
            set_bit += 1
        n = n // 2
    return set_bit

print(hammingWeight(2147483645))