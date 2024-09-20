# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        list1 = []
        list2 = []
        def invertor(root, lisst):
            if root.left == None and root.right == None:
                lisst.append(root.val)
                return
            if root.left:
                invertor(root.left,lisst)
            if root.right:
                invertor(root.right,lisst)
        invertor(root1, list1)
        invertor(root2, list2)
        if list1 == list2:
            return True
        return False

        