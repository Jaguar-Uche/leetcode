from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        arr = [[0]*n for _ in range(m)]

        def confirm_coordinates(k,l):
            is_okay = True
            if k < 0 or k >= m or l < 0 or l >= n:
                is_okay = False
            return is_okay

        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    if confirm_coordinates(i-1,j-1):
                        arr[i-1][j-1] +=1
                    if confirm_coordinates(i-1,j):
                        arr[i-1][j] +=1
                    if confirm_coordinates(i-1,j+1):
                        arr[i-1][j+1] +=1
                    if confirm_coordinates(i,j-1):
                        arr[i][j-1] +=1
                    if confirm_coordinates(i,j+1):
                        arr[i][j+1] +=1
                    if confirm_coordinates(i+1,j-1):
                        arr[i+1][j-1] +=1
                    if confirm_coordinates(i+1,j):
                        arr[i+1][j] +=1
                    if confirm_coordinates(i+1,j+1):
                        arr[i+1][j+1] +=1
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    if arr[i][j] < 2:
                        board[i][j] = 0
                    elif arr[i][j] <= 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                else:
                    if arr[i][j] == 3:
                        board[i][j] = 1
