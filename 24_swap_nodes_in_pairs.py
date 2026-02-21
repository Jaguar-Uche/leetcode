from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        seen_nodes = 0
        while head:
            seen_nodes += 1
            if seen_nodes % 2 == 0:
                nums.insert(seen_nodes-2, head.val)
            else:
                nums.append(head.val)
            head = head.next
        dummy = ListNode()
        head = dummy
        for i in range(len(nums)):
            head.next = ListNode(nums[i])
            head = head.next
        return dummy.next