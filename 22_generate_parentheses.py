from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr = [""]
        i = 1

        while i <= n:
            curr_arr = arr.copy()
            arr = []
            seen = set()  # reset each level
            for s in curr_arr:
                # insert "()" at every possible position
                for idx in range(len(s) + 1):
                    check = s[:idx] + "()" + s[idx:]
                    if check not in seen:
                        seen.add(check)
                        arr.append(check)

            print(arr)
            print(f"it has length of {len(arr)}")
            i += 1
        return arr


solution = Solution()
solution.generateParenthesis(4)
