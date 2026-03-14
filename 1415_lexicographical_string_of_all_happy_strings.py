class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        s = ['a', 'b', 'c']
        count = 0

        def build(current):
            nonlocal count

            if len(current) == n:
                count += 1
                if count == k:
                    return current
                return None

            for letter in s:
                if current and letter == current[-1]:
                    continue

                ans = build(current + letter)
                if ans:
                    return ans

            return None

        ans = build("")
        return ans if ans else ""


solution = Solution()
print(solution.getHappyString(n=3, k=9))
