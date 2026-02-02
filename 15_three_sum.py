from typing import List
def two_sum(nums: List[int], target: int) -> List[int]:
    val =[]
    check_set = set()
    for i in range(len(nums)):
        if target - nums[i] in check_set:
            val.append([nums[i], target-nums[i]])
        else:
            check_set.add(nums[i])
    return val

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        threeSum = []
        for i in range(len(nums)):
            arr= nums[:i] + nums[i+1:]
            result = two_sum(arr, -nums[i])
            if len(result) >=1:
                for res in result:
                    d = [nums[i], *res]
                    if d not in threeSum:
                        threeSum.append(d)
        return threeSum

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))