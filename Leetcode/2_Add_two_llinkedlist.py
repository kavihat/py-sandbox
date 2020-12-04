# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        t = s = None

        temp1 = l1
        temp2 = l2
        carry = 0
        while temp1 or temp2:

            if temp1 is None and temp2 is not None:
                tot = temp2.val + carry

            elif temp2 is None and temp1 is not None:
                tot = temp1.val + carry

            else:
                tot = temp1.val + temp2.val + carry

            sum = tot % 10
            carry = tot // 10
            p = ListNode(sum)
            if s is None:
                s = p
                t = p
            else:
                t.next = p
                t = t.next

            temp1 = temp1.next if temp1 else None
            temp2 = temp2.next if temp2 else None
        if carry:
            p = ListNode(carry)
            t.next = p
            t = t.next
        return s
