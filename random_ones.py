# import time
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# # first_time = time.time()
# # print(fib(35))
# # end_time = time.time()
# # print(end_time - first_time)
#
# # print()
# # print()
# memo = {1:1, 2:1}
# def memoize_fib(n):
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n] = fib(n)
#         return memo[n]
# #
# # start_time = time.time()
# # print(memoize_fib(35))
# # end_time = time.time()
# # print(end_time - start_time)
# #
# # print()
# # print()
#
# def bottom_up_fib(n):
#     if n <= 2:
#         return 1
#     arr = [0]*(n+1)
#     arr[1] = 1
#     arr[2] = 1
#     for i in range(3, n+1):
#         arr[i] = arr[i-1] + arr[i-2]
#     return arr[n]
#
# start_time = time.time()
# print(bottom_up_fib(100))
# end_time = time.time()
# print()
# print(end_time - start_time)
#
#
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# A function that passes information upwards, and then returns a value at end


# import bisect
#
#
# class Interval:
#     def __init__(self, start, finish, weight):
#         self.start = start
#         self.finish = finish
#         self.weight = weight
#
#     def __repr__(self):
#         return f"({self.start}, {self.finish}, w={self.weight})"
#
#
# def weighted_interval_scheduling(intervals):
#     # Step 1: Sort intervals by finish times
#     intervals.sort(key=lambda x: x.finish)
#     n = len(intervals)
#
#     # Step 2: Extract finish times to easily binary search over them
#     finish_times = [job.finish for job in intervals]
#
#     # M[i] stores the optimal value using the first i intervals
#     M = [0] * (n + 1)
#
#     # Step 3: Fill dynamic programming table
#     for i in range(1, n + 1):
#         current_job = intervals[i - 1]
#
#         # Binary search to find the latest non-overlapping interval.
#         # We look for a finish time <= current_job.start.
#         # bisect_right finds the insertion point, moving 1 index ahead.
#         idx = bisect.bisect_right(finish_times, current_job.start)
#
#         # Calculate options
#         include_val = current_job.weight + M[idx]
#         exclude_val = M[i - 1]
#
#         M[i] = max(include_val, exclude_val)
#     return M[n]
#
#
# # --- Demonstration ---
# # if __name__ == "__main__":
# jobs = [
#         Interval(5,8,1),
#         Interval(6,7,7),
#         Interval(4,7,3),
#         Interval(9,10,6),
#         Interval(7,8,2),
#         Interval(11,14,3),
#         Interval(3,5,5)
#     ]
# # [(1,3,2),(4,5,2),(1,5,5),(6,9,3),(6,7,1),(8,9,1)]
#
# max_profit = weighted_interval_scheduling(jobs)
# print(f"Maximum Profit: {max_profit}")


def palindrome_checker(s):
    left = 0
    right =len(s) - 1
    while left <= right:
        if s[left] == s[right]:
            left += 1
            right -= 1
            continue
        else:
            return False
    return True

def all_palindromes(s):
    left = 0
    arr = []
    for j in range(len(s)):
        t = j
        while left <= t:
            if s[left] == s[t]:
                left += 1
                t -=1
            else:
                break
        if left > t:
            arr.append(s[:j+1])
        left = 0
    return arr

print(all_palindromes("ababa"))
