# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        dct = {}
        se = set()
        temp = head
        pre = None
        while temp:
            if temp.val not in dct:
                dct[temp.val] = 1
                pre = temp
            else:
                dct[temp.val] += 1
                se.add(temp.val)
                pre.next = temp.next

            temp = temp.next
        temp2 = head
        pre = None
        while temp2:
            if temp2.val not in se:
                pre = temp2
            else:
                if pre is not None:
                    pre.next = temp2.next
                else:
                    head = head.next

            temp2 = temp2.next

        return head
