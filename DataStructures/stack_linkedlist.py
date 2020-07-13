# Implementing Stack using Linked list in Python
# Functions like push,pop and traversal implemented

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.top = None
        self.next = None

    def push(self, item):
        if self.top is None:
            self.top = Node(item)
        else:
            temp = Node(item)
            temp.next = self.top
            self.top = temp

    def pop(self):
        if self.top is None:
            print('Stack is empty')
        else:
            print('Popped element is ' + self.top.data)
            self.top = self.top.next

    def traverse(self):
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next


st = stack()
st.push('a')
st.push('b')
st.push('c')
st.traverse()
print('Pushing e')
st.push('e')
st.traverse()
print('removing e')
st.pop()
st.pop()
st.pop()
st.pop()
st.pop()
