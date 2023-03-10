# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root):
        if root == None:
            return 0
        
        return 1+max(self.helper(root.left),self.helper(root.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return self.helper(root)
