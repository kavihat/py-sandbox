# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dct={}
        temp=head
        pre=None
        while temp:
            if temp.val not in dct:
                dct[temp.val]=1
                pre = temp
            else:
                dct[temp.val]+=1
                pre.next=temp.next

            temp=temp.next
        return head