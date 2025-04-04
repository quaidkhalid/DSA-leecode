# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # stack = []
        # inorder = []
        # while root or stack:
        #     if root:
        #         stack.append(root)
        #         root = root.left
        #     else:
        #         root = stack.pop()
        #         inorder.append(root.val)
        #         root = root.right
        # return inorder 
        result = []
        def travers(root):
            if root:
                travers(root.left)
                result.append(root.val)
                travers(root.right)

        travers(root)
        return result