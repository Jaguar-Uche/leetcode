class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n > 0:
            default_x = x
            while n > 1:
                x *=default_x
                n-=1
        else:
            default_x = x = 1/ x
            n = -n
            while n > 1:
                x *=default_x
                n-=1
        return x

s = Solution()
print(s.myPow(2,-3))