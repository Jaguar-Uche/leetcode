from typing import List
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        i = 0
        while i < len(asteroids):
            if mass < asteroids[i]:
                return False
            mass += asteroids[i]
            i += 1
        return True

solution = Solution()
print(solution.asteroidsDestroyed(mass = 5, asteroids = [4,9,23,4]))


def asteroidsDestroyed(mass: int, asteroids: List[int]) -> bool:
    mx = max(asteroids)
    while asteroids:
        uneaten = []
        for aster in asteroids:
            if mass < aster:
                uneaten.append(aster)
            else:
                mass += aster
                if mass >= mx:
                    return True
        if len(uneaten) == len(asteroids):
            return False
        asteroids = uneaten
    return True




print(sum([False, False, False]))

