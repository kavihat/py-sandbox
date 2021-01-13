class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
def deleteMiddleNode(head):
    temp=head
    pre=None
    cur=temp
    k=1
    mid=lengthOfNode(temp)//2
    while temp:
        if k==mid:
            pre.next=cur.next
            k+=1
        else:
            pre=cur
            cur=cur.next
            k+=1
        temp=temp.next


def lengthOfNode(head):
    if head is None:
        return 0
    else:
        return (1+lengthOfNode(head.next))
def disp(temp):
    while temp:
        print(temp.val)
        temp=temp.next

inputlist=Node(1,Node(2,Node(3,Node(4))))
deleteMiddleNode(inputlist)
disp(inputlist)