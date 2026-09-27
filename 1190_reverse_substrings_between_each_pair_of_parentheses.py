class Solution:
    def reverseParentheses(self, s: str) -> str:
        s_arr = list(s)
        start_index = []
        result = ""
        n = len(s)
        for i in range(n):
            if s[i] == "(":
                start_index.append(i)
            if s[i] == ")":
                start = start_index.pop()
                end = i
                while start < end:
                    s_arr[start], s_arr[end] = s_arr[end], s_arr[start]
                    start += 1
                    end -= 1
        for char in s_arr:
            if char != ")" and char != "(":
                result += char
        return result
sol = Solution()
print(sol.reverseParentheses("(ed(et(oc))el)"))