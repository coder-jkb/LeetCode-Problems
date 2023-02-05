# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root1,root2):
        if root1==None and root2==None:
            return True

        elif (root1==None and root2!=None) or (root2==None and root1!=None):
            return False

        elif root1.val != root2.val:
            return False

        left = self.helper(root1.left,root2.right)
        if left==False:
            return False
        right = self.helper(root1.right,root2.left)
        if right==False:
            return False
        return left and right 

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:      
        return self.helper(root,root)

            