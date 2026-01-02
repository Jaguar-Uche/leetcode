def threeSum(nums):
    nums.sort()
    zeros = []
    positive_numbers = []
    negative_numbers = []
    for number in nums:
        if number > 0:
            positive_numbers.append(number)
        elif number == 0:
            zeros.append(number)
        elif number < 0:
            negative_numbers.append(number)
    if len(zeros) > 2:
        three_sums_array = [[0,0,0]]
    else:
        three_sums_array = []
    for index, num in enumerate(negative_numbers):
        difference = abs(num)
        if difference in positive_numbers and len(zeros) > 0:
            to_add = [num, difference, 0]
            to_add.sort()
            if to_add not in three_sums_array:
                three_sums_array.append(to_add)
        for i in range(len(negative_numbers)):
            if i == index:
                continue
            next_difference = difference - negative_numbers[i]
            if next_difference in positive_numbers:
                to_add = [num, negative_numbers[i], next_difference]
                to_add.sort()
                if to_add not in three_sums_array:
                    three_sums_array.append(to_add)

    return three_sums_array



print(threeSum([-1,0,1,2,-1,-4]))

