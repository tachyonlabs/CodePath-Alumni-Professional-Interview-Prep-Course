# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        """
        On one hand, I thought, how is this a graph problem, it is just doing a level-order
        traversal of a binary tree and returning an array of arrays of the data on each level.
        But I guess it's the 2D array that is the graph.
        """
        queue = deque([(A, 0)])
        results = []
        row = []
        depth = 0
        while queue:
            current, current_depth = queue.popleft()
            if current_depth == depth:
                row.append(current.val)
            else:
                results.append(row[:])
                row = [current.val]
                depth = current_depth
            if current.left:
                queue.append((current.left, depth + 1))
            if current.right:
                queue.append((current.right, depth + 1))

        if row:
            results.append(row)

        return results
