# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        def deconstruct_linked_list(l):
            current = l
            value = []
            while current is not None:
                value.append(current.val)
                current = current.next
            value.reverse()
            print(value)
            number = 0
            for i in range(len(value)):
                number += value[i] * (10 ** (len(value) - i - 1))
            return number

        def construct_linked_list(list):
            head = None
            current = None
            for i in range(len(list)):
                if not head:
                    head = ListNode(list[i])
                else:
                    if i == 1:
                        head.next = ListNode(list[i])
                        current = head.next
                    else:
                        current.next = ListNode(list[i])
                        current = current.next
            return head

        sum = deconstruct_linked_list(l1) + deconstruct_linked_list(l2)
        string_sum = str(sum)
        value_list = []
        for i in range(len(string_sum)):
            value_list.append(int(string_sum[i]))
        value_list.reverse()

        return construct_linked_list(value_list)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next