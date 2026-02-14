class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        arr_of_glasses = [[0]* (k+1) for k in range(query_row + 1)]
        arr_of_glasses[0][0] = poured
        for i in range(query_row+1):
            if i == query_row:
                is_row = True
            else:
                is_row = False
            j = 0
            while j <= i:
                if arr_of_glasses[i][j] > 1:
                    diff = arr_of_glasses[i][j] -1
                    arr_of_glasses[i][j] = 1
                    if i + 1 <= query_row:
                        arr_of_glasses[i + 1][j] += diff/ 2
                        arr_of_glasses[i + 1][j + 1] += diff/ 2
                if is_row:
                    if j == query_glass:
                        return arr_of_glasses[i][j]
                j +=1


s = Solution()
print(s.champagneTower(100000009,33,17))