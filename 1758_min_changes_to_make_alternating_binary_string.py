def changes_one(s):
    arr = list(s)
    n = len(arr)
    moves = 0
    if arr[0] == '0':
        moves += 1
        arr[0] = '1'
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            if arr[i] == '0':
                arr[i] = '1'
            else:
                arr[i] = '0'

            moves += 1
    return moves

def changes_zero(s):
    arr = list(s)
    n = len(arr)
    moves = 0
    if arr[0] == '1':
        moves += 1
        arr[0] = '0'
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            if arr[i] == '0':
                arr[i] = '1'
            else:
                arr[i] = '0'

            moves += 1
    return moves
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0
        s,t = changes_zero(s), changes_one(s)
        return min(s,t)

solution = Solution()
print(solution.minOperations("1111"))