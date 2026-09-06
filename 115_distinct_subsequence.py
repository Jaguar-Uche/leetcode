# I will explain the test cases here their indices from s string by their left, and in bracket their possible indices in the t string:
# for Rabbbit, trying to get rabbit.
#     0 r(0) is the first letter of our t string
#     1 a(1) can be attached to that r
#     2 b(2) can be attached to that a
#     3 b(3, 2) can be attached to the b as 3 or to a as 2
#     4 b(3, 3, 2) can be attached to the previous b as 3 or to the b before that as 3, or to a as 2
#     5 i(4,4,4) can be attached to the 2 3s from previous one or to the 3 from the b before previous
#     6 t(5,5,5) can only be attached to the previous t
# for babgbag to get bag
#     0 b(0) is the first letter of our t string
#     1 a(1) is the second letter of our t string
#     2 b(0) is the first letter of our t string
#     3 g(2) continues from 1 a to form a complete string which gives us one subsequence
#     4 b(0) could start a new string
#     5 a(1,1, 1) could continue 0 b or continue 2 b or 4 b
#     6 g(2,2,2,2) could continue the 3 from 5 a or continue 2 1 a to give us 4 complete strings
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[0] = 1

        for char in s:
            for i in range(len(t) - 1, -1, -1):
                if char == t[i]:
                    dp[i + 1] += dp[i]

        return dp[len(t)]

sol = Solution()
print(sol.numDistinct(s = "babgbag", t = "bag"))