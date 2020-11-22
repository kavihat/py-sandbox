# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10)

        while l1.next or l2.next or c:
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            val = l1.val + l2.val + c
            c = val // 10
            ret = ListNode(val % 10)

            ret.next = self.addTwoNumbers(l1.next, l2.next, c)
        return ret


s = Solution()
l1 = ListNode(3, ListNode(4, ListNode(5, None)))
l2 = ListNode(4, ListNode(6, ListNode(2, None)))
while l1:
    print(l1.val)
    l1=l1.next
sum_of_nodes = s.addTwoNumbers(l1, l2)
print(int(sum_of_nodes.val))

#
# run = True
#         count=1
#         if A not in B:
#             return -1
#         while run:
#             if B in A:
#                 run = False
#                 return count
#
#             else:
#                 A=A+A
#                 count=count+1