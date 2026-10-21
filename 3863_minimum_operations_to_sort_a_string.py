class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        min_char = "z"
        max_char = "a"
        char_indices = {}
        if s == "".join(sorted(s)) or n == 1:
            return 0
        if n == 2:
            return -1
        for index, char in enumerate(s):
            if ord(char) < ord(min_char):
                min_char = char
            if ord(char) > ord(max_char):
                max_char = char
            char_indices.setdefault(char, []).append(index)
        if s[0] == min_char or s[n-1] == max_char:
            return 1
        if (len(char_indices[min_char]) == 1 and char_indices[min_char] == [n-1]) and (len(char_indices[max_char]) == 1 and char_indices[max_char] == [0]):
            return 3
        return 2

sol = Solution()
print(sol.minOperations("edc"))