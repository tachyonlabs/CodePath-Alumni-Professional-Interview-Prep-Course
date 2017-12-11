# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        if not A:
            return 0

        queue = deque([(A, 0)])
        while queue:
            current, total = queue.popleft()
            if not current.left and not current.right and current.val + total == B:
                return 1
            if current.left:
                queue.append((current.left, current.val + total))
            if current.right:
                queue.append((current.right, current.val + total))

        return 0
