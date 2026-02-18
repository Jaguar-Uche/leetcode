from typing import List

def binary_search_with_direction(nums: List[int], target: int, first = True) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            if first:
                check_first = binary_search_with_direction(nums[:mid], target, first)
                if check_first == -1:
                    return mid
                else:
                    return check_first
            else:
                check_last = binary_search_with_direction(nums[mid+1:], target, False)
                if check_last == -1:
                    check_last = mid
                else:
                    check_last += mid+1
                return check_last
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first_occurance = binary_search_with_direction(nums[:mid], target)
                second_occurance = binary_search_with_direction(nums[mid + 1:], target, False)
                if first_occurance == -1:
                    first_occurance = mid
                if second_occurance == -1:
                    second_occurance = mid
                else:
                    second_occurance += mid + 1
                return [first_occurance, second_occurance]

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [-1, -1]

solution = Solution()
print(solution.searchRange(nums=[5, 7, 7, 8, 8, 8, 9], target=7))

# Functions that helped
def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        if nums[mid] > target:
            right = mid - 1
    return -1
def binary_search_first(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            check_in_first = binary_search_first(nums[:mid], target)
            if check_in_first == -1:
                return mid
            else:
                return check_in_first
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_last(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            check_last = binary_search_last(nums[mid+1:], target)
            if check_last == -1:
                return mid
            else:
                return check_last+mid+1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find_first_and_last(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            first_occurance = binary_search_with_direction(nums[:mid], target)
            second_occurance = binary_search_with_direction(nums[mid + 1:], target, False)
            if first_occurance == -1:
                first_occurance = mid
            if second_occurance == -1:
                second_occurance = mid
            else:
                second_occurance += mid + 1
            return [first_occurance, second_occurance]

        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return [-1, -1]

