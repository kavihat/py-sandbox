class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# Iteration
def kthElement(k, head):
    temp = head
    counter = 1
    if k > lengthOfList(temp):
        print("Invalid Input")
    while temp:
        if k <= counter:
            print(temp.val)
        counter += 1
        temp = temp.next


def lengthOfList(head):
    if head is None:
        return 0
    else:
        return (1 + lengthOfList(head.next))


input_list = Node(1, Node(2, Node(3, Node(7, Node(8)))))
kthElement(4, input_list)


# Recursiion

def kthElement(head, k, counter):
    temp = head
    if temp is None:
        return None
    else:
        if k == counter:
            return temp
        else:
            counter += 1
            return kthElement(temp.next, k, counter)


def disp(head):
    temp = head
    while temp:
        print(temp.val)
        temp = temp.next


input_list = Node(1, Node(2, Node(3, Node(7, Node(8)))))
output = kthElement(input_list, 4, 1)
disp(output)
