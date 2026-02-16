class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        map = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
        }
        def convert(num: str):
            m = 1
            num_int = 0
            for i in range(len(num) - 1, -1, -1):
                num_int += map[num[i]] * m
                m *= 10
            return num_int

        return str(convert(num1) * convert(num2))

solution = Solution()
print(solution.multiply("2", "3"))
print(solution.multiply("123", "456"))