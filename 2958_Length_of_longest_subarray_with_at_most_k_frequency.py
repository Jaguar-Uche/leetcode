from typing import List

# Find the good subarrays, and track only the length of the largest good subarray seen
    # How to find good subarrays?
    # count the elements in the subarray
    # start left pointer at the beginning
    # create a hashmap with number and frequency, whenever you count new one, you add it and check if it is greater than the k
    # if not continue counting,
    # if yes, we move the pointer, from the first element, and keep subtracting, until we get to the element whose subtraction reduces k back to an acceptable range, and then the total, if gre
# ater than the global total, we update it

    # If any is more than k, we remove the first element, and if the first element removal makes the frequency less than k, then it is fine,
    # if not, then we remove another one after it, until we remove the one that makes it less than k, then move forward the right pointer
# return the largest length of good subarray encountered
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left, right, n = 0,0, len(nums)
        global_total = float('-inf')
        check_map = {'total': 0}
        while right < n:
            print(f"right:{right} is less than n:{n}")
            check_map[nums[right]] = check_map.get(nums[right], 0) + 1
            check_map['total'] +=1
            print(f"check_map:{check_map}")
            if check_map[nums[right]] > k:
                print(f"The frequency of {nums[right]} is greater than k:{k}")
                global_total = max(global_total, check_map['total'] - 1)
                print(f"global_total becomes {global_total}")
                focus = nums[right]
                print(f"focus is {focus}")
                seen = 0
                while check_map[focus] > k:
                    print(f"Current value of left is {left}")
                    if nums[left] == focus:
                        seen += 1
                        check_map[focus] -= 1
                        check_map['total'] -= seen
                        left += 1
                        print(f"Left has changed to {left}")
                    else:
                        check_map[nums[left]] -= 1
                        seen += 1
                        left += 1
            right+=1
            print()
        print(f"global_total is {global_total}")
        print(f"Check_map is {check_map}")
        global_total = max(global_total, check_map['total'])
        return global_total
solution = Solution()
print(solution.maxSubarrayLength([1,2,2,1,3], 1))
