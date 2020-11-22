# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        return helper(root, 1)


def helper(root: TreeNode, type) -> int:
    if not root.left and root.right:
        if type:
            return root.val
        else:
            return 0
    res = 0
    if root.left:
        res += helper(root.left, 1)
    if root.right:
        res += helper(root.right, 0)
    return res
