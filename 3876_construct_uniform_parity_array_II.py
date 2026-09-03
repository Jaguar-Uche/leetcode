class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        smallest_odd = float("inf")
        smallest_even = float("inf")

        for num in nums1:
            if num % 2:
                smallest_odd = min(smallest_odd, num)
            else:
                smallest_even = min(smallest_even, num)

        can_odd = smallest_odd < smallest_even
        can_even = smallest_odd == float("inf")

        return can_odd or can_even
