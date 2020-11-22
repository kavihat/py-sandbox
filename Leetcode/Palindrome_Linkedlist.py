class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return False
        temp1 = head
        temp2=ListNode(temp1.val)
        while temp1:
            if temp1==head:
                temp2=ListNode(temp1.val)
                head2=temp2

            else:
                temp2=ListNode(temp1.val)
                temp2.next=head2
                head2=temp2
            temp1=temp1.next


        ispalindrome=True
        temp1=head
        while temp1:
            if temp1.val==temp2.val:
                temp1=temp1.next
                temp2=temp2.next
            else:
                ispalindrome=False
                break

        return ispalindrome


s = Solution()
print(s.isPalindrome(None))

