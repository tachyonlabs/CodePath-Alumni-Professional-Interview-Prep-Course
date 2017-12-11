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
    def maxDepth(self, A):
        if not A:
            return 0
        max_d = 1
        depth = 1
        queue = deque([[A, depth]])
        while queue:
            current, depth = queue.popleft()
            max_d = max(max_d, depth)
            if current.left:
                queue.append([current.left, depth + 1])
            if current.right:
                queue.append([current.right, depth + 1])

        return max_d
