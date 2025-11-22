
def intersectionSizeTwo(intervals):
    dictionary = {}
    minimum_set = set()
    for current_interval in intervals:
        occurence_list = []
        for num in range(current_interval[0], current_interval[1] + 1):
            count_num = 0
            if num in minimum_set:
                # print(f"{num} is in minimum_set")
                if len(occurence_list) == 0 or len(occurence_list) == 1:
                    occurence_list.append(num)
                    # print(f"{num} appended")
                elif len(occurence_list) == 2:
                    num_one = occurence_list[0]
                    num_two = occurence_list[1]
                    num_one_occurence = dictionary.get(num_one)
                    num_two_occurence = dictionary.get(num_two)
                    number_occurence = dictionary.get(num)
                    if number_occurence > num_one_occurence and number_occurence > num_two_occurence:
                        minimum_occurence = min(num_one_occurence, num_two_occurence)
                        if num_one in minimum_set:
                            new_dictionary = {num_two: num_two_occurence, num_one: num_one_occurence}
                        else:
                            new_dictionary = {num_one: num_one_occurence,num_two: num_two_occurence}
                        smaller_num = get_key_by_value(new_dictionary, minimum_occurence)
                        if smaller_num == num_one:
                            occurence_list[0] = num
                            # print(f"{num_one} has been replaced with {num}")
                        elif smaller_num == num_two:
                            occurence_list[1] = num
                            # print(f"{num_two} has been replaced with {num}")
                    elif number_occurence > num_one_occurence:
                        occurence_list[0] = num
                        # print(f"{num_one} has been replaced with {num}")
                    elif number_occurence > num_two_occurence:
                        occurence_list[1] = num
                        # print(f"{num_two} has been replaced with {num}")
                    else:
                        pass
                # print(occurence_list)
                continue
            for interval in intervals:
                if num in dictionary.keys():
                    count_num = dictionary[num]
                    break
                if num < interval[0] or num > interval[1]:
                    continue
                else:
                    count_num += 1
            dictionary[num] = count_num
            if len(occurence_list) == 2:
                num_one = occurence_list[0]
                num_two = occurence_list[1]
                current_num_occurence = count_num
                num_one_occurence = dictionary.get(num_one)
                num_two_occurence = dictionary.get(num_two)
                # print(f"the occurence of {num_one} is {num_one_occurence}")

                # print(f"the occurence of {num_two} is {num_two_occurence}")
                # print(f"the occurence of {num}(current) is {count_num}")

                if current_num_occurence > num_one_occurence and current_num_occurence > num_two_occurence:
                    minimum_occurence = min(num_one_occurence, num_two_occurence)
                    if num_one in minimum_set:
                        new_dictionary = {num_two: num_two_occurence, num_one: num_one_occurence}
                    else:
                        new_dictionary = {num_one: num_one_occurence, num_two: num_two_occurence}
                    smaller_num = get_key_by_value(new_dictionary, minimum_occurence)
                    # print(f"The number with less occurence is {smaller_num}")

                    if smaller_num == num_one:
                        occurence_list[0] = num
                    elif smaller_num == num_two:
                        occurence_list[1] = num
                elif current_num_occurence > num_one_occurence:
                    occurence_list[0] = num
                    # print(f"{num} has replaced {num_one} in the list")
                elif current_num_occurence > num_two_occurence:
                    occurence_list[1] = num
                    # print(f"{num} has replaced {num_two} in the list")
                else:
                    pass
                # print()
            else:
                occurence_list.append(num)
                # print(f"{num} appended cause list is less than 2")
        # print(dictionary)
        # print(minimum_set)
        # print(occurence_list)

        for number in occurence_list:
            minimum_set.add(number)
    return len(minimum_set)

def get_key_by_value(dictionary, target_value):
    for key, value in dictionary.items():
        if value == target_value:
            return key
    return None  # Return None if the value is not found

print(intersectionSizeTwo([[1,3],[3,7],[5,7],[7,8]]))