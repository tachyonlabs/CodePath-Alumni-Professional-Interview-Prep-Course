# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, A):
        if not (A):
            return 0

        queue = deque([[A, 1]])
        while queue:
            current, depth = queue.popleft()
            if not current.left and not current.right:
                return depth
            if current.left:
                queue.append([current.left, depth + 1])
            if current.right:
                queue.append([current.right, depth + 1])
