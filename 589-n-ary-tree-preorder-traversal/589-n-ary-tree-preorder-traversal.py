"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # self , left to right
        ans = []
        def pre(root):
            if root:
                ans.append(root.val)
                
                if root.children:
                    for child in root.children:
                        pre(child)
                    
        pre(root)
        return ans
            