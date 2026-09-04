# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # cleaner, O(n) solution
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr: Optional[TreeNode]) -> int:
            if not curr: 
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            # updates self.res if available
            self.res = max(self.res, (left + right))

            # returns height
            height = 1 + max(left,right)
            return height

        # calls the recursive function starting from the root
        dfs(root) 
        return self.res
