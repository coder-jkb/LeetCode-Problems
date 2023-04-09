# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        s = 0
        if root:
            left = root.left
            # if left is a leaf node 
            if left and left.left == None and left.right == None:
                s += left.val
            
            return s + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        
        return 0