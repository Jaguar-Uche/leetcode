from typing import List
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        res = []
        balance = 0
        start = 0
        # split into top-level mountains
        for i, ch in enumerate(s):
            if ch == '1':
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                # recursively process the inside
                inner = s[start + 1:i]
                fixed_inner = self.makeLargestSpecial(inner)
                res.append("1" + fixed_inner + "0")
                start = i + 1

        # sort descending to make lexicographically largest
        res.sort(reverse=True)
        return "".join(res)

solution = Solution()
# print(ret_special_substrings("1110110000"))
print(solution.makeLargestSpecial("110110001100"))
# print(handle_long_mountain("1100"))