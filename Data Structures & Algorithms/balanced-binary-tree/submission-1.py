# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True 
        def dfs(curr):
            if not curr: 
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            # update res
            diff = abs(left - right)
            if diff > 1: 
                nonlocal res
                res = False

            # return height
            height = 1 + max(left, right)
            return height

            # alternatively can make the recursive fn return [boolean, height], and then just return dfs(root)[0] which would give the boolean. no need for the res member var

        dfs(root)
        return res
        