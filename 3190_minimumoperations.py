def minimumOperations(nums) -> int:
    min_operations = 0
    for number in nums:
        if number % 3 != 0:
            min_operations += 1

    return min_operations

print(minimumOperations([3,6,9]))