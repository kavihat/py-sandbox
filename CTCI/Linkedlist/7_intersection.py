class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def intersetction(temp1, temp2):
    shortNode=temp1 if lengthOfList(temp1) < lengthOfList(temp2) else temp2
    largeNode =  temp2 if lengthOfList(temp1) < lengthOfList(temp2) else temp1
    diff = lengthOfList(largeNode) - lengthOfList(shortNode)
    for i in range(diff):
        largeNode=largeNode.next

    while largeNode!=shortNode:
        shortNode=shortNode.next
        largeNode=largeNode.next
    return largeNode



def lengthOfList(head):
    if head is None:
        return 0
    else:
        return 1+lengthOfList(head.next)

def disp(head):
    if head is None:
         print("None")
    while head:
        print(head.val)
        head = head.next

# sub_list=Node(5, Node(6, Node(3)))
list2 =  Node(8,Node(9))
inp_list = Node(1, Node(2, Node(3, Node(4))))
output = intersetction(inp_list,list2)
disp(output)
