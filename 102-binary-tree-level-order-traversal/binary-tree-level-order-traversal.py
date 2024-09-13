# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        Q = []
        elements = []
        Q.append(root)

        while Q:
            size = len(Q)
            level_elements = []

            for i in range(size):
                item = Q.pop(0)

                if item.left:
                    Q.append(item.left)
                if item.right:
                    Q.append(item.right)
                level_elements.append(item.val)

            elements.append(level_elements)
        return elements
            

                


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if not root:
        #     return []

        # Q = []
        # elements = []
        # Q.append(root)

        # while Q:
        #     x = len(Q)
        #     level_element = []

        #     for i in range(x):
        #         item = Q.pop(0)
                
        #         if item.left:
        #             Q.append(item.left)
        #         if item.right:
        #             Q.append(item.right)

        #         level_element.append(item.val)

        #     elements.append(level_element)

        # return elements      