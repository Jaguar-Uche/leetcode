def maxSumDivThree(nums) -> int:
    nums.sort()
    print(nums)
    total = sum(nums)
    if total % 3 == 0:
        return total
    else:
        max_sums = []
        for i,num in enumerate(nums):
            for index in range(len(nums)):
                new_list= nums[index:i+1]
                half_sum = sum(new_list)
                if (total - half_sum) % 3 == 0:
                    max_sums.append(total - half_sum)
                if i != index:
                    second_sum = num + nums[index]
                    if (total - second_sum) % 3 == 0:
                        max_sums.append(total - second_sum)

        highest = max(max_sums)

        return highest or 0
print(maxSumDivThree([2,3,36,8,32,38,3,30,13,40]))
print(sum([2,3,36,8,32,38,3,30,13,40]))


def maxSumDivThree(nums):
    total = sum(nums)

    # Lists of numbers by remainder
    rem1 = []
    rem2 = []

    for x in nums:
        if x % 3 == 1:
            rem1.append(x)
        elif x % 3 == 2:
            rem2.append(x)

    # Sort them so we can pick smallest
    rem1.sort()
    rem2.sort()

    if total % 3 == 0:
        return total

    res = 0

    if total % 3 == 1:
        # Option 1: remove smallest remainder 1
        option1 = rem1[0] if rem1 else float('inf')

        # Option 2: remove two smallest remainder 2
        option2 = sum(rem2[:2]) if len(rem2) >= 2 else float('inf')

        res = total - min(option1, option2)

    else:  # total % 3 == 2
        # Option 1: remove smallest remainder 2
        option1 = rem2[0] if rem2 else float('inf')

        # Option 2: remove two smallest remainder 1
        option2 = sum(rem1[:2]) if len(rem1) >= 2 else float('inf')

        res = total - min(option1, option2)

    return res if res != float('inf') else 0
