def check_dic(diction):
    check = None
    for key,value in diction.items():
        if check is None:
            check = value
        if value != check:
            return False
    return True

a ={}
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        for i in range(n):
            distinct_letters = {s[i]: 1}
            for j in range(i+1, n):
                distinct_letters[s[j]] = distinct_letters.get(s[j], 0) + 1
                if check_dic(distinct_letters):
                    max_len = max(max_len, j-i+1)
        return max_len
solution = Solution()
print(solution.longestBalanced("zzabccy"))
