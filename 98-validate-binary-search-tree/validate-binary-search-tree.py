# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # make a function to check it is bst or not 
        def valid(root,min_val,max_val):
            # base case
            if not root:
                return True
            #base case
            if not (min_val<root.val<max_val):
                return False
            # recursive call
            return valid(root.left,min_val,root.val) and valid(root.right,root.val,max_val)
            
        return valid(root,float('-inf'),float('inf'))
        