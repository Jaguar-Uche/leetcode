from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        current = head
        previous = None
        while current:
            if current.val in seen:
                previous.next = current.next
                current = current.next
            else:
                previous = current
                current = current.next
                seen.add(current.val)
        return head
