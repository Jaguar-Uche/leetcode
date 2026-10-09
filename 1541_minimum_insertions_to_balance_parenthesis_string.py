class Solution:
    def minInsertions(self, s: str) -> int:
        opening = []
        seen = 0
        result = 0
        for index, char in enumerate(s):
            # print(index)
            # print(char)
            if char == '(':
                # print("I have encountered an opening bracket")
                # print(opening)
                if seen != 0:
                    # print(f"I have seen {seen} consecutive closing brackets")
                    # If We have encountered a closing bracket
                    if seen % 2 == 0:
                        # print(f"Seen is a multiple of 2, hence i add {seen // 2}")
                        # If the consecutive closing brackets is a multiple of 2, we just need 1 for each of them
                        result += (seen //2)
                    elif seen % 2 == 1:
                        # print(f"seen is an odd number so i add {2 + seen //2}")
                        if len(opening) > 0:
                            result += 1
                        else:
                            result += 2
                        result += seen // 2
                        # If the consecutive closing brackets is an odd number, we need half for the even portion, and 2 for the odd portion
                        # result += (2 + seen // 2)
                    # print("any opening bracket that has not been attended to cannot be attended to anymore, so we set opening bracket to [] and seen to 0")
                    opening = []
                    seen = 0
                # Store the opening bracket index
                # print("I store the opening bracket's index in opening")
                opening.append(index)
                # print(opening)
            else:
                # print("I have encountered an closing bracket")
                # print(f"seen {seen} closing brackets")
                if len(opening) > 0:
                    # print("There is a current opening bracket that has not been attended to")
                    # If there is an opening bracket that has not been attended to
                    if seen == 1:
                        # print("I have already seen one opening bracket, so this one completes it, nothing to be added to result, i remove the opening, and then i set seen to 0")
                        # If there was an immediate closing bracket before this.
                        opening.pop()
                        # We have used the current ones
                        seen = 0
                    elif seen == 0:
                        # print("we have not seen any previous closing bracket")
                        # No preceding opening bracket, we have one opening bracket now
                        seen += 1
                else:
                    # No opening bracket, seen becomes one
                    # print('There is no opening bracket unattended to')
                    seen +=1
            # print()
        if seen > 0:
            result += (( seen % 2 + seen // 2 )- len(opening))
        else:
            result += ( 2 * len(opening))
        return result

sol = Solution()
# print(sol.minInsertions("(()))"))


def minInsertions(s: str) -> int:
    opening = []
    seen = 0
    result = 0
    for index, char in enumerate(s):
        if char == '(':
            if seen == 0:
                opening.append(index)
                continue
            elif seen == 1:
                if len(opening) > 0:
                    opening.pop()
                    result += 1
                else:
                    result += 2
            elif seen == 2:
                result += 1
            else:
                if seen % 2 == 0:
                    result += (seen //2)
                else:
                    result += (seen // 2 + 2)
            seen = 0
            opening.append(index)
        else:
            if seen == 1:
                if len(opening) > 0:
                    opening.pop()
                    seen = 0
                else:
                    seen += 1
            else:
                seen += 1
    if seen == 0:
        pass
    elif seen == 1:
        if len(opening) > 0:
            opening.pop()
            result += 1
        else:
            result += 2
    elif seen == 2:
        result += 1
    else:
        if seen % 2 == 0:
            result += (seen // 2)
        else:
            result += (seen // 2 + 2)
    result += (2 * len(opening))
    return result

print(minInsertions("(()))(()))()())))"))
