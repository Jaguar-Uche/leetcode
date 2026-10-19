class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        res = []
        # print(nums)
        for i in range(len(nums)):
            if nums[i] > target:
                break
            if nums[i] == target:
                res.append(i)
        # left, right = 0, len(nums) - 1
        # while left <=  right:
        #     mid = (left + right) // 2
        #     print(f"mid = {mid} and nums[mid] = {nums[mid]}")
        #     if nums[mid] > target:
        #         print(f"{nums[mid]} > {target}")
        #         print(f"{right} becomes {mid-1}")
        #         right = mid -1
        #
        #     if nums[mid] < target:
        #         print(f"{nums[mid]} < {target}")
        #         print(f"{left} becomes {mid + 1}")
        #         left = mid + 1
        #     if nums[mid] == target:
        #         res.append(mid)
        #         n = 1
        #         is_left, is_right = True, True
        #         while True:
        #             if is_left and mid -n >= 0 and nums[mid - n] == target:
        #                 # print(nums[mid-n])
        #                 # print("The right is equal to target")
        #                 res.append(mid - n)
        #             else:
        #                 # print("The left is not equal to target")
        #                 # print("False")
        #                 is_left = False
        #             if is_right and mid +n < len(nums) and nums[mid + n] == target:
        #                 # print("The right is equal to target")
        #                 res.append(mid + n)
        #             else:
        #                 # print("The right is not equal to target")
        #                 is_right = False
        #             if is_left or is_right:
        #                 # print("There is a left or a right")
        #                 n += 1
        #             else:
        #                 # print("BReak")
        #                 break
        #         left = right + 2
        # return sorted(res)
        return res

sol = Solution()
print(sol.targetIndices([1,2,5,2,3], 5))