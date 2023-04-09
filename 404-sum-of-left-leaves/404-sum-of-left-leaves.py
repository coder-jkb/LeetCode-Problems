# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,node):
        s = 0
        if node:
            left = node.left
            # if leaf node
            if left and left.left == None and left.right == None:
                s += left.val
            
            return s + self.helper(node.left) + self.helper(node.right)
        
        return 0
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)