from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous = dummy
        move = True
        while head.next:
            if move:
                previous = previous.next
            move = not move
            head = head.next
        previous.next = previous.next.next
        return dummy.next


def traverse_linked_list(head: ListNode):
    if head is None:
        print(None)
        return
    while head:
        print(head.val, end='->')
        head = head.next

a = ListNode(1)
b = ListNode(3)
c= ListNode(4)
d = ListNode(7)
e = ListNode(1)
f = ListNode(2)
g = ListNode(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
solution = Solution()
traverse_linked_list(solution.deleteMiddle(a))


