# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invertor(root):
    if root.left == None and root.right == None:
            return root.val
    left = invertor(root.left)
    right = invertor(root.right)

    if root.val == 3:
        return (left and right)
    if root.val == 2:
        return (left or right)

    

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return invertor(root)
        
        