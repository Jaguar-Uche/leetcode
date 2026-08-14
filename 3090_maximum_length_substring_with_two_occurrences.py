class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left, right, n = 0,0, len(s)
        global_total = 0
        check_map = {'total':0}
        while right < n:
            focus = s[right]
            check_map[focus] = check_map.get(focus, 0) + 1
            check_map['total'] += 1
            if check_map[s[right]] > 2:
                global_total = max(global_total, check_map['total'] - 1)
                seen = 0
                while check_map[focus] > 2:
                    if s[left] == focus:
                        seen += 1
                        check_map[focus] -= 1
                        check_map['total'] -= seen
                        left += 1
                    else:
                        check_map[s[left]] -= 1
                        seen += 1
                        left += 1
            right += 1

        max_length = max(global_total, check_map['total'])
        return max_length

sol = Solution()
print(sol.maximumLengthSubstring("aaaa"))