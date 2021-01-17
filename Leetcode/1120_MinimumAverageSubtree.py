# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    max_average = -float('inf')

    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.helper(root)
        return self.max_average

    def helper(self, root: TreeNode):
        if not root:
            self.max_average = max(self.max_average, 0)
            return [0, 0]

        lsum, rsum = 0, 0
        lcount, rcount = 0, 0
        if root.left:
            [lsum, lcount] = self.helper(root.left)
        if root.right:
            [rsum, rcount] = self.helper(root.right)
        current_subtree_sum = (lsum + rsum + root.val)
        current_subtree_count = (lcount + rcount + 1)
        current_subtree_avg = current_subtree_sum / current_subtree_count
        self.max_average = max(current_subtree_avg, self.max_average)
        return [current_subtree_sum, current_subtree_count]
