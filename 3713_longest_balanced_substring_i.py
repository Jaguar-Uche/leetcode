class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0

        for i, char in enumerate(s):
            hash_seen = {}
            highest_seen = 0
            for j in range(i+1, n):
                hash_seen[s[j]] = hash_seen.get(s[j], 0) + 1
                if hash_seen[s[j]] > highest_seen:
                    highest_seen = hash_seen[s[j]]

