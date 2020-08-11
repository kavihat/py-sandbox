"""Binary Search Tree relies on property where elements greater than root node lies towards right of the node and
lesser than root lies towards left of node.
Here inorder traversal has been used to display the elements of tree after insertion
find method is defined to find if an element is present in tree or not
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class binarysearchtree:
    def __init__(self, key):
        self.root = Node(key)

    def insert(self, key, root):
        # Node(key)
        if root:

            if key.val < root.val:
                if root.left is None:
                    root.left = key
                else:
                    return self.insert(key, root.left)
            elif key.val > root.val:
                if root.right is None:
                    root.right = key
                else:
                    return self.insert(key, root.right)

    def preorder(self, root):
        output = []
        if root:
            output.append(root.val)
            output += self.preorder(root.left)
            output += self.preorder(root.right)
        return output

    def find(self, root, data):
        if root:
            if data == root.val:
                return True
            elif data < root.val:
                if root.left:
                    return self.find(root.left, data)
                else:
                    return False
            elif data > root.val:
                if root.right:
                    return self.find(root.right, data)
                else:
                    return False


r = Node(50)
b = binarysearchtree(r)
b.insert(Node(20), r)
b.insert(Node(60), r)
b.insert(Node(40), r)
print(b.find(r, 20))
print(b.preorder(r))
