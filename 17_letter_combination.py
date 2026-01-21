from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_hash = {
            "1": '',
            "2": 'abc',
            "3": 'def',
            "4": 'ghi',
            "5": 'jkl',
            "6": 'mno',
            "7": 'pqrs',
            "8": 'tuv',
            "9": 'wxyz',
        }
        arr = []
        while digits:
            if not arr:
                for letter in letter_hash[digits[0]]:
                    arr.append(letter)
            else:
                second_array = []
                if digits[0] != '1':
                    for word in arr:
                        for second_letter in letter_hash[digits[0]]:
                            second_array.append(word + second_letter)
                    arr = second_array.copy()
            digits = digits[1:]
        return arr

sol = Solution()
print(sol.letterCombinations('23'))