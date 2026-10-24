class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        month_length = [31, 28, 31, 30, 31, 30,
                        31, 31, 30, 31, 30, 31]

        def later_date(a, b):
            month_a, day_a = map(int, a.split("-"))
            month_b, day_b = map(int, b.split("-"))

            if month_a > month_b:
                return a
            if month_b > month_a:
                return b

            return a if day_a >= day_b else b

        def earlier_date(a, b):
            month_a, day_a = map(int, a.split("-"))
            month_b, day_b = map(int, b.split("-"))

            if month_a < month_b:
                return a
            if month_b < month_a:
                return b

            return a if day_a <= day_b else b

        def day_difference(start, end):
            start_month, start_day = map(int, start.split("-"))
            end_month, end_day = map(int, end.split("-"))

            if start_month == end_month:
                return end_day - start_day + 1

            days = month_length[start_month - 1] - start_day + 1
            days += end_day

            for month in range(start_month, end_month - 1):
                days += month_length[month]

            return days

        latest_arrival = later_date(arriveAlice, arriveBob)
        earliest_leave = earlier_date(leaveAlice, leaveBob)

        if latest_arrival > earliest_leave:
            return 0

        return day_difference(latest_arrival, earliest_leave)

sol = Solution()
print(sol.countDaysTogether(arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"))