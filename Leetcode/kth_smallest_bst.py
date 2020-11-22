class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:


    def kthSmallest(self, root: TreeNode, k: int) -> int:

        limit = k
        res = self.inorder(root,k)
        return res[limit-1]

    def inorder(self, root, k):
        res=[]
        if root:
            res += self.inorder(root.left,k)
            res.append(root.val)
            if len(res)>=k:
                return res
            res += self.inorder(root.right,k)
        return res


s = Solution()
print(s.kthSmallest(TreeNode(3, TreeNode(1), TreeNode(4)), 3))

'''
3 [[[[],0,[]], 1, [[],2,[]]], 3, [[],4,[]]]
'''

