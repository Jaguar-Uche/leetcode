from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        res = []
        trial = []
        while head:
            trial.append(head)
            head = head.next
            if len(trial) == k:
                res.append(*reversed(trial))
                trial = []
        dummy = ListNode()
        head = dummy
        for i in range(len(res)):
            head.next = ListNode(res[i])
            head = head.next
        return dummy.next


class Soltn:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # find kth node
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            # reverse group
            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # reconnect
            tmp = group_prev.next  # old head becomes tail
            group_prev.next = kth  # new head of group
            group_prev = tmp  # move to next group