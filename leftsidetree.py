class TreeNode:
  def __init__(self,key):
    self.left = None
    self.right = None
    self.val = key
def visible_nodes(root):
    # Write your code here
    dct = {}
    output = []
    depth = 0
    if root is None:
        return 0
    if depth == 0:
        dct[depth] = root.val
    return helper(root, dct, depth)


def helper(root, dct, depth):
    if depth not in dct:
        dct[depth] = root.val
    if root.left:
        return helper(root.left, dct, depth + 1)
    if root.right:
        return helper(root.right, dct, depth + 1)
    output = list(dct.values())
    print(output)
    print(dct)
    print(depth)
    return len(output)


root_1 = TreeNode(8)
root_1.left = TreeNode(3)
root_1.right = TreeNode(10)
root_1.left.left = TreeNode(1)
root_1.left.right = TreeNode(6)
root_1.left.right.left = TreeNode(4)
root_1.left.right.right = TreeNode(7)
root_1.right.right = TreeNode(14)
root_1.right.right.left = TreeNode(13)
print(visible_nodes(root_1))