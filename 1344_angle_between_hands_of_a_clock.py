class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        closest_hour_to_minutes_time = minutes // 5
        offset_from_minutes_time = minutes - (closest_hour_to_minutes_time * 5)

        minute_angle=(closest_hour_to_minutes_time * 30+ offset_from_minutes_time * 6)

        hour_angle = (hour % 12) * 30 + minutes * 0.5

        total_angle = abs(minute_angle - hour_angle)

        return min(total_angle, 360 - total_angle)

solution = Solution()
print(solution.angleClock(hour = 4, minutes = 22))
