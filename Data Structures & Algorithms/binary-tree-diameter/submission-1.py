# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0

        return 1 + max(
            self.depthOfBinaryTree(root.left),
            self.depthOfBinaryTree(root.right)
        )

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root: 
            return 0

        tmp = self.depthOfBinaryTree(root.left) + self.depthOfBinaryTree(root.right)
        diameter = max(
            tmp, 
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right)
            )
        return diameter

    
    
        