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
    def verticalOrderTraversal(self, A):
        """
        I thought I would do a BFS, adding node values to lists in a dict, with the negative
        (left) or positive (right) distance from the root being the keys. BFS would
        automatically put the values at each distance in the order the problem wanted. Then I
        returned a list of the lists sorted by key. Very fast and simple to write.
        InterviewBit's solution hint took this approach as well, and noted that it was an
        O(nlogn) solution due to needing to sort the hash.
        """
        if not A:
            return []

        lines = {}
        queue = deque([(A, 0)])
        while queue:
            current, line = queue.popleft()
            lines[line] = lines.get(line, []) + [current.val]
            if current.left:
                queue.append((current.left, line - 1))
            if current.right:
                queue.append((current.right, line + 1))

        return [lines[key] for key in sorted(lines.keys())]