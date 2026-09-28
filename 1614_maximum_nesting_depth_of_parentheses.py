class Solution:
    def maxDepth(self, s: str) -> int:
        left_seen = 0
        right_seen = 0
        max_seen = 0
        for char in s:
            if char == "(":
                left_seen += 1
            elif char == ")":
                right_seen += 1
                left_seen -= 1
                right_seen -= 1
            max_seen = max(max_seen, left_seen - right_seen ,  right_seen if right_seen == left_seen else 0)
        return max_seen

sol = Solution()
print(sol.maxDepth("()(())((()()))"))