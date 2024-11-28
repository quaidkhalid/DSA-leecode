# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root_val = preorder[0]
        root_val_index = inorder.index(root_val)

        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[1:root_val_index + 1], inorder[:root_val_index])
        root.right= self.buildTree(preorder[root_val_index + 1:], inorder[root_val_index + 1:])
        
        return root
        