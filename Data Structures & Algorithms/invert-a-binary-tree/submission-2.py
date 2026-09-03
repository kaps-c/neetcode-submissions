# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # cleaner version
        # no need pointer since root is just the node

        if root is None: 
            return None

        # if the left and right are swapped and both are none then root will be empty, so it's fine to simply swap them then let the previous case handle it

        # no need the else statement because it'll happen if it's not the if case
        # swap
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

