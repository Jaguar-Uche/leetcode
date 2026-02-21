from typing import Optional, List
from Heap_Method import MinHeap
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums =[]
        for list in lists:
            if list is None:
                pass
            else:
                while list is not None:
                    nums.append(list.val)
                    list = list.next

        nums.sort()
        head = ListNode()
        for i in range(len(nums)):
            head.next = ListNode(nums[i])
            head = head.next
        return head.next


class Stn:
    def mergeKLists(self, lists):
        heap = MinHeap()

        uid = 0
        for node in lists:
            if node:
                heap.push((node.val, uid, node))
                uid += 1

        dummy = ListNode(0)
        cur = dummy

        while heap:
            val, _, node = heap.pop()

            cur.next = node
            cur = cur.next

            if node.next:
                heap.push((node.next.val, uid, node.next))
                uid += 1

        return dummy.next

sol