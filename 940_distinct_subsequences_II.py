class Solution:
    def distinctSubseqII(self, s: str) -> int:
        seen = set()
        seen.add(s[0])
        arrs = [[s[0]]]
        no = 1
        for i in range(1, len(s)):
            letter = s[i]
            local_arr = []
            if letter not in seen:
                local_arr.append(letter)
                seen.add(letter)
                no += 1
                no %=1000000007
            for arr in arrs:
                for el in arr:
                    el+=letter
                    if el not in seen:
                        no+=1
                        no %=1000000007
                        seen.add(el)
                        local_arr.append(el)
            # print(local_arr)
            arrs.append(local_arr)
            # print(arrs)
        return no

sol = Solution()
print(sol.distinctSubseqII("aba"))