class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        letter_map = {'a': False, 'b': False, 'c': False, 'd': False, 'e': False, 'f': False, 'g': False, 'h': False,
                      'i': False, 'j': False, 'k': False, 'l': False, 'm': False, 'n': False, 'o': False, 'p': False,
                      'q': False, 'r': False, 's': False, 't': False, 'u': False, 'v': False, 'w': False, 'x': False,
                      'y': False, 'z': False}
        seen = set()
        for letter in word:
            if letter.isupper():
                if letter in seen:
                    letter_map[letter.lower()] = True
            else:
                seen.add(letter)
        return sum(letter_map[k] for k in letter_map)

solution = Solution()
print(solution.numberOfSpecialChars("aaAbcBC"))
