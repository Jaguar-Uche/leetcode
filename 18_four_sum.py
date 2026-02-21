from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            arr = three_sum(nums, i+1, target-nums[i])

            for triple in arr:
                result.append([nums[i]] + triple)

        return result


def three_sum(nums: List[int], start: int, target: int) -> List[List[int]]:
    res = []

    for i in range(start, len(nums)-2):
        if i > start and nums[i] == nums[i-1]:
            continue

        left, right = i+1, len(nums)-1

        while left < right:
            s = nums[i] + nums[left] + nums[right]

            if s == target:
                res.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1

            elif s < target:
                left += 1
            else:
                right -= 1

    return res


solution = Solution()
print(solution.fourSum([-3,-2,-1,0,0,1,2,3], 0))