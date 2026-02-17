from typing import List
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def bitcount(num):
            return bin(num).count('1')
        result = []
        for hour in range(12):
            for minute in range(60):
                if bitcount(hour) + bitcount(minute) == turnedOn:
                    result.append(str(hour)+':'+str(minute).zfill(2))
        return result

solution = Solution()
print(solution.readBinaryWatch(1))