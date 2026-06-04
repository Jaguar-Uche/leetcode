def waviness(num) -> int:
    total = 0
    num = str(num)
    for i in range(1, len(num)-1):
        if num[i] > num[i-1] and num[i] > num[i+1] or num[i] < num[i-1] and num[i] < num[i+1]:
            total += 1
    return total

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total = 0
        for i in range(num1, num2+1):
            total += waviness(i)
        return total

solution = Solution()
print(solution.totalWaviness(4848, 4848))