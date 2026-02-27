from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        changed = False
        def change(index):
            num = nums[index]
            for j in reversed(range(index+1, n)):
                if nums[j] > num:
                    nums[index] = nums[j]
                    nums[j] = num
                    reverse(index + 1)
                    break

        def reverse(index):
            left = index
            right = n - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        for i in reversed(range(n-1)):
            if nums[i] < nums[i+1]:
                change(i)
                changed = True
                break
        if not changed:
            nums.reverse()

solution = Solution()
solution.nextPermutation([1,2,4,3])