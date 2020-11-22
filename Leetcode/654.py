"""
 Maximum Binary Tree
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums):
        return self.helper(nums,0,len(nums)-1)


    def helper(self, nums, start, end):
        if start>end:
            return None
        if start == end:
            return TreeNode(nums[start], None, None)

        max = 0
        max_index = start
        for i in range(start,end+1):
            if nums[i] >= max:
                max = nums[i]
                max_index = i

        return  TreeNode(max, self.helper(nums, start, max_index - 1),
                        self.helper(nums, max_index + 1, end))



s = Solution()
output = s.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
print(output)
