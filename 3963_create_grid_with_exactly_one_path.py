class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = []
        for i in range(m):
            to_append = ""
            for j in range(n):
                if i == 0:
                    to_append+='.'
                else:
                    if j == n-1:
                        to_append+="."
                    else:
                        to_append+="#"
            res.append(to_append)
        return res

sol = Solution()
print(sol.createGrid(1,1))