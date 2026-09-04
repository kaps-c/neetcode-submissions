# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # iterative bfs - cleaner ver

        # initialise deques
        dp = deque([p])
        dq = deque([q])

        while dp:
            # FIFO
            dp_curr = dp.popleft()
            dq_curr = dq.popleft()

            # ignore null nodes
            if not dp_curr and not dq_curr:
                continue

            if not dp_curr or not dq_curr:
                return False
            
            # check if nodes are the same
            if dp_curr.val != dq_curr.val:
                return False

            # add children of current node to queues only if they're equal
            dp.extend([dp_curr.left, dp_curr.right])
            dq.extend([dq_curr.left, dq_curr.right])
        
        return True

        