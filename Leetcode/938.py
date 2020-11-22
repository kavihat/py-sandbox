class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        result = 0
        if root:
            lsum = self.checker(root.left, L, R)
            rsum = self.checker(root.right, L, R)
            if root.val >= L and root.val <= R:
                result = root.val
            result = lsum + rsum + result
        return result

    def checker(self, root, L, R):
        if root.val >= L and root.val <= R:
            return root.val
        elif root.val<=R:
            return self.checker(root.right)
        else:
            return False



# sum = 0
# if root:
#     if root.val >= L:
#         if root.val >= L and root.val <= R:
#             sum=sum+root.val
#
#         return self.rangeSumBST(root.left, L, R)
#     elif root.val<=R:
#         if root.val>=L and root.val<=R:
#             sum=sum+root.val
#         if root.right:
#             return self.rangeSumBST(root.right,L,R)
#         else:
#             return False
#     else:
#         return False
# return True
#
#
