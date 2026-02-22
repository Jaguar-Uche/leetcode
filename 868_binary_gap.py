class Solution:
    def binaryGap(self, n: int) -> int:
        first_one = None
        second_one = None
        i = 1
        diff = 0
        while n:
            if n & 1:
                if first_one is None:
                    # print("First one is None")
                    first_one = i
                    print(f"Hence first one is {first_one}")
                else:
                    if second_one is None:
                        print("Second one is None")
                        second_one = i
                    else:
                        print("First and Second one are not none")
                        first_one = second_one
                        print(f"First one becomes {first_one}")
                        second_one = i
                        print(f"Second One becomes {second_one}")
            if first_one and second_one:
                diff = max(diff, second_one - first_one)
            n = n >> 1
            i+=1

        return diff

solution = Solution()
print(solution.binaryGap(5))
