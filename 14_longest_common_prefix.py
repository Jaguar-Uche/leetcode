def longestCommonPrefix(self, strs) -> str:
    len_strings = [(len(x) , index) for index,x in enumerate(strs)]
    least = min(len_strings)
    prefix = ""
    if min == 0:
        return prefix
    for i in range(least[0]):
        counter = 0
        for x in strs:
            if x[i] == strs[least[i]]:
                counter += 1
            else:
                break
        if counter == len(strs):
            prefix += least[i][i]
        else:
            break

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Sort to bring the most different strings to the ends
        strs.sort()

        first = strs[0]
        last = strs[-1]

        prefix = []

        # Compare characters until they differ
        for f, l in zip(first, last):
            if f == l:
                prefix.append(f)
            else:
                break

        return "".join(prefix)
