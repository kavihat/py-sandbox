class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def SumofLinkedList(head1, head2):
    carry = 0
    n = p = None
    temp1 = head1
    temp2 = head2
    while temp1 or temp2:
        tot = carry
        if temp1:
            tot += temp1.val
            temp1 = temp1.next
        if temp2:
            tot += temp2.val
            temp2 = temp2.next
        sum_ll = tot % 10
        carry = tot // 10
        k = Node(sum_ll)
        if n is None:
            n = k
            p = k
        else:
            p.next = k
            p = p.next

    return n


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



def disp(head):
    temp = head
    while temp:
        print(temp.val, end="")
        temp = temp.next


list1 = Node(7, Node(1, Node(6)))
list2 = Node(5, Node(9, Node(2)))
output,carry = sumofElements(list1, list2)
if carry:
    q=Node(carry)
    q.next=output
    output=q
disp(output)

# recursion



