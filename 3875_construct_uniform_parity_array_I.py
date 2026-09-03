class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        can_odd = True
        can_even = True
        odd_nums = 0
        even_nums = 0
        for num in nums1:
            if num % 2 == 0:
                even_nums+=1
            else:
                odd_nums+=1
        if odd_nums == 1:
            can_even = False
        if odd_nums == 0 and even_nums >0:
            can_odd = False
        return can_odd or can_even

sol = Solution()
print(sol.uniformArray([1,2]))

