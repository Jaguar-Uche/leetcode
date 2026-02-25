from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        s ={}
        i = 0
        for word in strs:
            t = "".join(sorted(word))
            if t in s:
               res[s[t]].append(word)
            else:
                s[t] = i
                res.append([word])
                i+=1
        return res

# s = {1:"5", 2:"7", 3:"6", 4:"9", 5:"8"}
# all_s ={0: s}
# k =(s, 0)
# print(k)
# if s in all_s.values():
#     print("yes")
# # print(all_s)
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
