from typing import List

# Convert the String to an array, cause we can update arrays
# Go Through the queryIndices(i) and update s at queryIndices[i] with queryCharacters[i]
# After each query, check the longest repeating character length, and put it inside an array
# At the end, return an array of these things

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        def count(a):
            # Count the longest repeating character length and return it
            pointer = 1
            current_character = a[0]
            length = 1
            longest_length = 1
            while pointer < len(a):
                if a[pointer] == current_character:
                    length += 1
                else:
                    longest_length = max(longest_length, length)
                    current_character = a[pointer]
                    length = 1
                pointer += 1
            longest_length = max(longest_length, length)
            return longest_length
        s_array = list(s)
        arr = []
        for i in range(len(queryIndices)):
            s_array[queryIndices[i]] = queryCharacters[i]
            arr.append(count(s_array))
        return arr