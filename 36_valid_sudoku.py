from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns =[set(), set(), set(), set(), set(), set(), set(), set(), set()]
        rows = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        squares = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        for i in range(9):
            for j,letter in enumerate(board[i]):
                if letter != ".":
                    pos = (i // 3) * 3 + j // 3
                    if letter in columns[i] or letter in rows[j] or letter in squares[pos]:
                        return False
                    columns[i].add(letter)
                    rows[j].add(letter)
                    squares[pos].add(letter)
        return True

solution = Solution()
print(solution.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

