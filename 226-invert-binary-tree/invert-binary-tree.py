# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertor(root):
            if not root.left and not root.right:
                return
            if root.left:
                invertor(root.left)
            if root.right:
                invertor(root.right)
            root.left, root.right = root.right, root.left
        if not root:
            return None
        invertor(root)
        return root
            
        
        # if not root:
        #     return

        # root.left, root.right = root.right, root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)       
        
        # return root