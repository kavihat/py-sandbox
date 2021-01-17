class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:

        return self.helper(root, target)[1]

    def helper(self, root: TreeNode, target: float):
        if not root:
            return [float('inf'), float('inf')]
        if not root.left and not root.right:
            return [abs(target - root.val), root.val]

        lval, lnode = self.helper(root.left, target)
        rval, rnode = self.helper(root.right, target)
        minval = min(lval, rval, abs(target - root.val))

        if minval == lval:
            minNode = lnode
        elif minval == rval:
            minNode = rnode
        else:
            minNode = root.val

        return [minval, minNode]


root = TreeNode(9)
root.left = TreeNode(6)
root.right = TreeNode(10)
root.right.right = TreeNode(11)
root.left.left = TreeNode(12)
root.left.right = TreeNode(5)

s = Solution()
print(s.closestValue(root, 3.7))
