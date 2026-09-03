# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pointer = root

        if root is None: 
            return None

        if (pointer.left is None) and (pointer.right is None):
            return root

        else:
            right = pointer.right
            left = pointer.left

            pointer.left = right
            pointer.right = left

            self.invertTree(pointer.left)
            self.invertTree(pointer.right)
        
        return root

