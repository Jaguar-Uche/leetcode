def maxSubarraySum(nums, k: int) -> int:
    highest = len(nums)
    check_len = highest if highest % k == 0 else highest - (highest % k)
    length_divisible = set()
    number_sums = set()
    while check_len > 0:
        length_divisible.add(check_len)
        check_len -= k
    for x in length_divisible:
        for i in range(highest - x+1):
            number_sums.add(sum(nums[i:i + x]))
    return max(number_sums) or 0

print(maxSubarraySum([1,2],1))
print(maxSubarraySum([-1,-2,-3,-4,-5],4))
print(maxSubarraySum([-5,1,2,-3,4],2))
