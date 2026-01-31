from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        index_of_target = alphabets.index(target)
        for i in range(index_of_target+1, 26):
            if alphabets[i] in letters:
                return alphabets[i]
        return letters[0]