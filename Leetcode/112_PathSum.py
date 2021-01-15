class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Node,summ):
        if root is None:
            if summ==0: return True
            else:
                return False

        else:
            summ-=root.val
            return self.hasPathSum(root.left,summ) or self.hasPathSum(root.right,summ)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
s=Solution()
print(s.hasPathSum(root,7))