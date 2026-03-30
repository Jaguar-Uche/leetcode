from collections import Counter
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1_set1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        s1_set2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        s2_set1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        s2_set2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        n = len(s1)
        for i in range(n):
            if i % 2 == 0:
                s1_set1[s1[i]] += 1
                s2_set1[s2[i]] += 1
            else:
                s1_set2[s1[i]] +=1
                s2_set2[s2[i]] += 1

        for i in range(ord('a'), ord('z') + 1):
            let = chr(i)
            if s1_set1[let] != s2_set1[let]:
                return False
            if s1_set2[let] != s2_set2[let]:
                return False
        return True

solution = Solution()
print(solution.checkStrings("yviqgzqwetjqwnmmbupitdsjdvophjhkiivtbsgehlxzestjjrqwahxcaafafgdxjiocwgnqbmoxbcbpiwz", "yjowhiiitgdesjzjwvqqnuonirjggtbpjmpwmzapjsbcqahxfidqoxotbavmfzbcblxvesxwgcahhqwkedi"))
