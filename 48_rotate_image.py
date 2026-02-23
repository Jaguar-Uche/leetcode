from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        arr = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(matrix[j][i])
            temp.reverse()
            arr.append(temp)
        for i in range(n):
            matrix[i] = arr[i]
        # Just to show us at the end
        print(matrix)



solution = Solution()
solution.rotate([[1,2,3],[4,5,6],[7,8,9]])