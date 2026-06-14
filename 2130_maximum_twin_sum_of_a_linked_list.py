# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        hashed_linked_list = {}
        index = 0
        max_sum = float('-inf')
        while head:
            hashed_linked_list[index] = head.val
            head = head.next
            index += 1
        n = len(hashed_linked_list)
        pivot = int(n/2)
        for i in range(pivot, n):
            t = n - i - 1
            if 0 <= t <= pivot -1:
                max_sum = max(max_sum, hashed_linked_list[i] + hashed_linked_list[t])
        return max_sum








