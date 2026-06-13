from typing import List
reverse_letters = [
  'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n',
  'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'
]
class Solution:
    def mapWordWeights(self, words:List[str], weights:List[int]) -> str:
        result = []
        for word in words:
            total = sum(weights[(ord(letter) & 31) -1] for letter in word) % 26
            result.append(reverse_letters[total])
        return ''.join(result)


solution = Solution()
print(solution.mapWordWeights(words = ["abcd","def","xyz"], weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]))