class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def Palindrome(temp1):
    temp2=temp1
    stk=[]
    flag=True
    while temp1:
        stk.append(temp1.val)
        temp1=temp1.next
    while temp2:
        cmp=stk.pop()
        if temp2.val==cmp:
            temp2=temp2.next
            continue
        else:
            flag=False
            break
    return flag




def disp(head):
    while head:
        print(head.val)
        head=head.next

input_list=Node(5,Node(2,Node(2,Node(1))))
output=Palindrome(input_list)
print(output)