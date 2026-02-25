from typing import List
def no_ones(n:int)->int:
    total = 0
    while n:
        if n & 1:
            total += 1
        n = n >> 1
    return total
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        res_array =[[], [], [], [], [], [], [], [], [], [], [], [], [],[]]
        for num in arr:
            ones = no_ones(num)
            # ones = num.bit_count()
            res_array[ones].append(num)
        # print(res_array)
        res = []
        for ran in res_array:
            res.extend(ran)
        return res

solution = Solution()
print(solution.sortByBits([0,1,2,3,4,5,6,7,8]))
# print(no_ones(8191))