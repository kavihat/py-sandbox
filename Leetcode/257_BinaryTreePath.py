class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def binaryTreePaths(self, root: TreeNode):
        l = []
        r = []
        if not root.left and not root.right:
            return [str(root.val)]
        else:
            if root.left:
                l = [str(root.val)+'->'+ x for x in self.binaryTreePaths(root.left)]
            if root.right:
                r = [str(root.val) + '->' + x for x in self.binaryTreePaths(root.right)]
            l.extend(r)
            return l


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
output = []
s = Solution()
print(s.binaryTreePaths(root))
