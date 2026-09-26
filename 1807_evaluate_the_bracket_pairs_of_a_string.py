class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Start by converting the knowledge to a hashmap so it is easier for us. and then we will
        # go and when we see a bracket, we keep a string for the key, and when the bracket closes, we use the full key
        hashmap = {}
        result = ""
        key = ""
        bracket_open = False
        for a,b in knowledge:
            hashmap[a] = b
        for char in s:
            if bracket_open:
                if char == ")":
                    bracket_open = False
                    result += hashmap.get(key, "?")
                    key = ""
                else:
                    key += char
            else:
               if char == "(":
                   bracket_open = True
               else:
                   result += char
        return result

sol = Solution()
print(sol.evaluate(s = "hi(name)", knowledge = [["a","b"]]))