# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root.left is None and root.right is None:
            return True
        if root.left:
            if root.val > root.left.val and root.val > max(root.left):
                return self.isValidBST(root.left)
            else:
                return False

        if root.right:
            if root.right.val > root.val > min(root.right):
                return self.isValidBST(root.right)
            else:
                return False
        else:
            return True


def min(root):
    min_t = float('inf')
    if root:
        if root.val < min_t:
            min_t = root.val
        min_t = min(root.left)

        return min_t


def tree_max(root):
    if root.right:
        max_t=root.right.val
    if root:
        if root.val>max_t:
            max_t=root.val
        max_t=tree_max(root.right)
    return max_t

root = TreeNode(12)
root.left = TreeNode(9)
root.right = TreeNode(15)
root.left.right = TreeNode(10)

print("Minimum element is",
      min(root))
print("maximum element is",
      tree_max(root))
