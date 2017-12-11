# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque


class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        if not A or (not A.left and not A.right):
            return True

        min_depth = None
        queue = deque([(A, 0)])
        while queue:
            current, current_depth = queue.popleft()
            if not current.left and not current.right:
                if not min_depth:
                    min_depth = current_depth
                    print "min =", min_depth,
                else:
                    print "current =", current_depth,
                    if current_depth - min_depth > 1:
                        return False

            else:
                if current.left:
                    queue.append((current.left, current_depth + 1))
                if current.right:
                    queue.append((current.right, current_depth + 1))

        return True
