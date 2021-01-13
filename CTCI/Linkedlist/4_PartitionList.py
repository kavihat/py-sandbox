class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        temp1 = temp2 = head
        p = n = None
        while temp1:
            if temp1.val < x:
                k = ListNode(temp1.val)
                if n is None:
                    p = k
                    n = k
                else:
                    p.next = k
                    p = p.next
            temp1 = temp1.next

        while temp2:
            if temp2.val >= x:
                k = ListNode(temp2.val)
                if n is None:
                    p = k
                    n = k
                else:
                    p.next = k
                    p = p.next
            temp2 = temp2.next
        return n