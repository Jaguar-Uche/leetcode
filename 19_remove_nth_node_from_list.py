# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr =[]
        while head:
            arr.append(head)
            head = head.next
        index_to_check = len(arr)-n-1
        if index_to_check <0:
            return arr[0].next
        else:
            # print(arr[index_to_check].val)
            arr[index_to_check].next = arr[index_to_check].next.next
        return arr[0]


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
s = Solution()
def show_values(head):
    while head:
        print(head.val)
        head = head.next
show_values(s.removeNthFromEnd(a, 5))