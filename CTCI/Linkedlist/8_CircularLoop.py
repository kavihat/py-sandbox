class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def circularLoop(temp):
    fast = temp
    slow = temp

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break
    if fast is None or fast.next is None:
        return None
    slow = temp
    while fast is not slow:
        fast = fast.next
        slow = slow.next
    return fast





# list1 = Node('a', Node('b', Node('c', Node('d', Node('e',list1)))))



a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d
d.next = a
output = circularLoop(a)
print(output.val)
