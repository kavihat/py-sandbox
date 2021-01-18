# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    lnode = None
    rnode = None
    l_end_node = None
    r_end_node = None

    def flatten(self, root: TreeNode) -> None:
        # left_subtree_node, left_end_node=self.helper(root.left)
        # right_subtree_node,right_end_node=self.helper(root.right)
        # root.right=left_subtree_node
        # left_end_node=right_subtree_node
        self.helper(root)


    def helper(self, root: TreeNode):
        if not root:
            return [None, None]
        if not root.left and not root.right:
            return [root, root]
        self.lnode ,  self.l_end_node = self.helper(root.left)
        self.rnode, self.r_end_node = self.helper(root.right)
        if self.lnode :
            root.right = self.lnode
            root.left = None
        if self.rnode:
            if  self.l_end_node:
                self.l_end_node = self.rnode
            root.right = self.rnode
            root.left = None
        temp = root

        while temp.right:
            temp = temp.right
        return (root, temp)


