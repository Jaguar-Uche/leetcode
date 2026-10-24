class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def convert_to_days(str_version):
            month = int(str_version[0:2])
            date = int(str_version[3:])
            total_days = sum(month_length[:month-1]) + date
            return total_days
        arrivealice_days = convert_to_days(arriveAlice)
        leavealive_days = convert_to_days(leaveAlice)

        arrive_bob_days = convert_to_days(arriveBob)
        leave_bob_days = convert_to_days(leaveBob)

        last_come = max(arrivealice_days, arrive_bob_days)
        first_leave = min(leavealive_days, leave_bob_days)
        if first_leave < last_come:
            return 0
        return first_leave - last_come + 1

sol = Solution()
print(sol.countDaysTogether(arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"))