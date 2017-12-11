# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        if not A or (not A.left and not A.right):
            return 1
        stack = []
        prev = None
        node = A
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if prev and prev >= node.val:
                    return False
                prev = node.val
                node = node.right

        return 1
