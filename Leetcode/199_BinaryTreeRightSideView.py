# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode):
        mydct = self.helper(root, 0, {})
        output = [mydct[k] for k in mydct]
        return output

    def helper(self, root: TreeNode, depth, dct):
        if not root:
            return None
        elif depth == 0:
            dct[depth] = root.val
        else:
            if depth in dct:
                dct[depth] = root.val

        self.helper(root.right, depth + 1, dct)
        self.helper(root.left, depth + 1, dct)

        return dct


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
s = Solution()
print(s.rightSideView(root))
