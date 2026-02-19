class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        substrings = 0
        runs = []
        zero_count = 0
        one_count = 0
        if s[0] == "0":
            zero_count += 1
        else:
           one_count += 1
        for i in range(1,n):
            if s[i] == '0':
                if s[i-1] == '0':
                    zero_count += 1
                else:
                    runs.append(one_count)
                    one_count = 0
                    zero_count = 1
            elif s[i] == '1':
                if s[i-1] == '1':
                    one_count += 1
                else:
                    runs.append(zero_count)
                    zero_count = 0
                    one_count = 1
        if one_count != 0:
            runs.append(one_count)
        elif zero_count != 0:
            runs.append(zero_count)
        for i in range(1, len(runs)):
            substrings += min(runs[i-1], runs[i])
        return substrings
solution = Solution()
print(solution.countBinarySubstrings("00011100"))