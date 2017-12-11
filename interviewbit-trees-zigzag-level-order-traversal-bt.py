# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers

    # note - v1 passed the efficiency tests just fine, but then when doing the writeup I noticed I
    # was doing some unnecessary steps, so I decided to clean that up here
    def zigzagLevelOrder(self, A):
        if not A:
            return []

        queue = deque([[A, 0]])
        zigzag = []
        level = []
        prev_depth = 0
        while queue:
            current_node, depth = queue.popleft()
            if level and depth != prev_depth:
                zigzag.append(level[:])
                level = []
                prev_depth = depth
            level.append(current_node.val)

            if current_node.left:
                queue.append([current_node.left, depth + 1])
            if current_node.right:
                queue.append([current_node.right, depth + 1])

        zigzag.append(level)

        return [row[::-1] if i % 2 else row for i, row in enumerate(zigzag)]
