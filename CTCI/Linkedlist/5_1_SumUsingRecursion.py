class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next



def sumofElements(temp1, temp2):
    carry=0
    tail=None
    if temp1.next is not None:
        tail,carry=sumofElements(temp1.next,temp2.next)
    tot=temp1.val+temp2.val+carry
    summ=tot%10
    carry=tot//10
    head=Node(summ)
    head.next=tail
    return head,carry

# def sumofElements(temp1, temp2):
#     if temp1.next is None:
#         tot = temp1.val + temp2.val
#         summ = tot % 10
#         carry = tot // 10
#         k = Node(summ)
#         return k, carry
#     else:
#         p, carry = sumofElements(temp1.next, temp2.next)
#         tot = temp1.val + temp2.val + carry
#         summ = tot % 10
#         carry = tot // 10
#         k = Node(summ)
#         k.next = p
#         return k, carry


def disp(head):
    temp = head
    while temp:
        print(temp.val, end="")
        temp = temp.next

def lengthOfList(head):
    if head is None:
        return 0
    else:
        return (1 + lengthOfList(head.next))

list1 = Node(7, Node(1, Node(6,Node(3))))
list2 = Node(5, Node(9, Node(2)))
smallesthead = list1 if lengthOfList(list1) < lengthOfList(list2) else list2
listdiff = abs(lengthOfList(list1) - lengthOfList(list2))
k=None
while listdiff:
    k = Node(0)
    k.next = smallesthead
    smallesthead=k
    listdiff -= 1
if lengthOfList(list1)<lengthOfList(list2):
    output,carry = sumofElements(smallesthead, list2)
else:
    output, carry = sumofElements(list1, smallesthead)


if carry:
    q=Node(carry)
    q.next=output
    output=q
disp(output)