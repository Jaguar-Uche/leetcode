class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_hash = {}
        magazine_hash = {}
        for letter in magazine:
            magazine_hash[letter] = magazine_hash.get(letter, 0) + 1
        for letter in ransomNote:
            ransom_hash[letter] = ransom_hash.get(letter, 0) + 1
        for letter in ransom_hash:
            if letter in magazine_hash:
                if ransom_hash[letter] <= magazine_hash[letter]:
                    pass
                else:
                    return False
            else:
               return False
        return True
