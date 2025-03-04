# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 1:
            return True
        elif root.val == 0:
            return False
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        if root.val == 3:
            return left and right
        elif root.val == 2:
            return left or right
            
        
        