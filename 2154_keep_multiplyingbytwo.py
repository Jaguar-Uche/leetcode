def findFinalValue(nums, original):
    num_set = set(nums)
    while original in num_set:
        original *= 2
    return original

nums = [2,7,9]
original = 4
print(findFinalValue(nums, original))