class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        path,diameter=self.helper(root)
        return diameter


    def helper(self,root:TreeNode):  # [path,subtree diameter]
        if not root:
            return [0,0]
        if not root.left and not root.right:
            return [1,0]
        lpath,rpath=0,0
        longpath=0
        diameter=0
        lsd,rsd=0,0
        if root.left:
            [lpath,lsd]= self.helper(root.left)
        if root.right:
            [rpath,rsd] = self.helper(root.right)
        longpath=1+max(lpath,rpath)
        diameter=lpath+rpath
        max_diameter=max(lsd,rsd,diameter)
        return [longpath,max_diameter]






root = TreeNode(1)
root.left = TreeNode(2)
root.right=TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
output = []
s = Solution()
print(s.diameterOfBinaryTree(root))