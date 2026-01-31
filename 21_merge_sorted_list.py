from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1, current2 = list1, list2
        if list1 is None:
            return list2
        linkedlist = ListNode(0)
        tail = linkedlist
        while current1 is not None and current2 is not None:
            if current1.val <= current2.val:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next
            tail = tail.next
        if current1 is not None:
            tail.next = current1
        if current2 is not None:
            tail.next = current2
        return linkedlist.next

s = Solution()
print(s.mergeTwoLists(ListNode(1,ListNode(2, ListNode(4))), ListNode(-1, ListNode(3, ListNode(4)))))