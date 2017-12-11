# Definition for a  binary tree node
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        return str(self.val)

from collections import deque


class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root:
            queue = deque([[root, 0]])
            current = None
            depth = 0
            while queue:
                prev, prev_depth = current, depth
                current, depth = queue.popleft()
                if prev and prev_depth == depth:
                    prev.next = current
                if current.left:
                    queue.append([current.left, depth + 1])
                if current.right:
                    queue.append([current.right, depth + 1])

        return root
