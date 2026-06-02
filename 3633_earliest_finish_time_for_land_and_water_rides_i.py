from typing import List
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int],waterDuration: List[int]) -> int:
        # Earliest possible completion of any land ride
        min_land_finish = min(start + duration for start, duration in zip(landStartTime, landDuration))

        # Best Land -> Water
        best_land_water = min(max(min_land_finish, start) + duration for start, duration in zip(waterStartTime, waterDuration))

        # Earliest possible completion of any water ride
        min_water_finish = min(start + duration for start, duration in zip(waterStartTime, waterDuration))

        # Best Water -> Land
        best_water_land = min(max(min_water_finish, start) + duration for start, duration in zip(landStartTime, landDuration))

        return min(best_land_water, best_water_land)
solution = Solution()
print(solution.earliestFinishTime(landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]))
