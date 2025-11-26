def convert(s: str, num_rows: int) -> str:
    limit = len(s)
    left_difference = 2 * num_rows
    right_difference = -2
    level = 1
    return_string = ""

    if num_rows == 1:
        return s

    while level <= num_rows:
        left_difference -= 2
        right_difference += 2
        current_index = level - 1

        while current_index < limit:
            # always append the first char
            if len(return_string) > 0:
                if s[current_index] != s[current_index + 1] and s[current_index] != s[current_index - 1]:
                    if return_string[-1] != s[current_index]:
                        return_string += s[current_index]
            else:
                return_string += s[current_index]


            # LEFT JUMP – only if non-zero
            if left_difference != 0:
                current_index += left_difference
                if current_index >= limit:
                    break
                return_string += s[current_index]
            else:
                # if left jump is zero, we should not do this jump at all
                # move to next iteration (but NOT continue early)
                # simply go to right jump section
                pass

            # RIGHT JUMP – only if non-zero
            if right_difference != 0:
                current_index += right_difference
                if current_index >= limit:
                    break
                return_string += s[current_index]

        level += 1

    return return_string


print(convert("PAYPALISHIRING", 3))
