# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        data=None
        temp1 = l1
        temp2 = l2
        n = p = None
        while temp1 or temp2:
            if temp1 is None and temp2 is not None:
                data = temp2.val
                temp2 = temp2.next if temp2 else None
            elif temp2 is None and temp1 is not None:
                data = temp1.val
                temp1 = temp1.next if temp1 else None
            elif temp1.val < temp2.val:
                data = temp1.val
                temp1 = temp1.next if temp1 else None
            elif temp1.val > temp2.val:
                data = temp2.val
                temp2 = temp2.next if temp2 else None
            elif temp1.val == temp2.val:
                data = temp1.val
                temp1 = temp1.next if temp1 else None
            k = ListNode(data)
            if n is None:
                n = k
                p = k
            else:
                p.next = k
                p = p.next
        return n
