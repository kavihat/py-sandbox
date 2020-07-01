class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class linkedlist:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def add(self, item):
        value = node(item)
        if self.head == None:
            self.head = value
        else:
            cur = self.head
            while (cur):
                pre = cur
                cur = cur.next
            pre.next = value

    def delete(self, item):
        cur = self.head
        print('deleting')
        while (cur):
            pre = cur
            cur = cur.next
            if cur is None:
                break
            # print('deleting')
            if cur.data == item:
                temp = cur.next
                pre.next = temp
                break


ll = linkedlist()
ll.add('a')
ll.add('b')
ll.add('c')
ll.add('d')
ll.add('d')
ll.delete('e')
ll.traverse()
