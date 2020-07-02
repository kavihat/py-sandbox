# Implement Linked list as a Queue - Data Structures
# Implemented functions to add elements to queue, delete inputted element from queue and display contents of queue


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        if self.rear is None:
            self.front = self.rear = Node(item)
        else:
            self.rear.next = Node(item)
            self.rear = self.rear.next

    def dequeue(self, item):
        if self.rear is None:
            print('Queue is empty')
        # elif self.front.data == item:
        #     self.front = self.front.next
        else:
            pre = self.front
            while pre:
                cur = pre.next
                if cur.data == item:
                    pre.next = cur.next
                    break
                elif pre.data == item:
                    # print(pre.data)
                    self.front = self.front.next
                    break

    def traverse(self):
        # print('reached here')
        while self.front:
            print(self.front.data)
            self.front = self.front.next


que = Queue()
que.enqueue('a')
que.enqueue('b')
que.enqueue('c')
que.dequeue('b')
que.enqueue('e')
que.dequeue('a')
que.traverse()
