# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # isSubtree: does subroot appear anywhere INSIDE?

        # are these the same tree starting HERE?
        def sameTree(root1, root2):
            # if both are none, you've reached the end - so return true
            if not root1 and not root2:
                return True
            
            # if root is alr done but root 2 isn't
            if not root1 or not root2:
                return False

            # if they're different values
            if root1.val != root2.val:
                return False

            # if they're the same value
            if root1.val == root2.val:
                left = sameTree(root1.left, root2.left)
                right = sameTree(root1.right, root2.right)
                return (left and right)

        # both trees are empty or sub tree is empty
        if not subRoot:
            return True

        # if only root is empty
        if not root:
            return False
        
        else: 
            if sameTree(root, subRoot):
                return True
            
            return (self.isSubtree(root.left, subRoot) or
                        self.isSubtree(root.right, subRoot))
        
        