# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def SumAndTilt(self, root, totalTilt):
        if not root:
            return 0
        leftsum = self.SumAndTilt(root.left, totalTilt)
        rightsum = self.SumAndTilt(root.right, totalTilt)
        tilt = abs(leftsum - rightsum)
        totalTilt[0] += tilt  # Using list to keep it mutable
        return root.val + leftsum + rightsum
    def findTilt(self, root: Optional[TreeNode]) -> int:
        totalTilt = [0]  # Mutable list to track the total tilt
        self.SumAndTilt(root, totalTilt)
        return totalTilt[0]
        
        