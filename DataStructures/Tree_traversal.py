class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class binaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def traversal(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder(tree.root)
        elif traversal_type == "inorder":
            return self.inorder(tree.root)
        elif traversal_type == "postorder":
            return self.postorder(tree.root)
        else:
            print("Invalid traversal type")

    def preorder(self, start):
        output = []
        if start:
            output.append(start.value)
            output += self.preorder(start.left)
            output += self.preorder(start.right)
        return output

    def inorder(self, start):
        output = []
        if start:
            output += self.inorder(start.left)
            output.append(start.value)
            output += self.inorder(start.right)
        return output

    def postorder(self, start):
        output = []
        if start:
            output += self.inorder(start.left)
            output += self.inorder(start.right)
            output.append(start.value)
        return output


tree = binaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.right.right = Node(5)

print(tree.traversal("preorder"))
print(tree.traversal("inorder"))
print(tree.traversal("postorder"))
