# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both empty
        if not p and not q:
            return True

        # one null one isn't null
        if not p or not q: 
            return False

        # values don't match (can condense into earlier false statement)
        if p.val != q.val: 
            return False
        
        # both trees are not empty and the values are the same
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))

        
        