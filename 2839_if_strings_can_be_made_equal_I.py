class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return (
            sorted([s1[0], s1[2]]) == sorted([s2[0], s2[2]]) and
            sorted([s1[1], s1[3]]) == sorted([s2[1], s2[3]])
        )

class Solution2:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        visited = set()
        def dfs(s):
            if s == s2:
                return True
            if s in visited:
                return False

            visited.add(s)

            op1 = s[2] + s[1] + s[0] + s[3]

            op2 = s[0] + s[3] + s[2] + s[1]

            return dfs(op1) or dfs(op2)

        return dfs(s1)

solution = Solution()
print(solution.canBeEqual("abcd", "cdab"))
