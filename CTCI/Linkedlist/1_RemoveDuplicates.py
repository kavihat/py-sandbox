class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
def removeDuplicates(head):
     temp=head
     curr=head
     pre=None
     while curr:
         delflag=False
         while temp!=curr:
             if temp.data!=curr.data:
                 temp=temp.next
             else:
                 pre.next=curr.next
                 delflag=True
                 break
         temp=head
         if not delflag:
             pre=curr
         curr=curr.next



def disp(head):
        temp = head
        while temp:
            print(temp.data)
            temp = temp.next

inp=Node(1,(Node(2,Node(2,Node(2,Node(3,Node(2)))))))
removeDuplicates(inp)
disp(inp)