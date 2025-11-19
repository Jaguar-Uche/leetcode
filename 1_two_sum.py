def twoSum(nums, target):
    seen = {}  # number → index

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i


array = [3,2,4]
target = int(input("Enter the target number: "))
print(twoSum(array,target))

