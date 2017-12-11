# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def recursive_invert(self, node):
        if node:
            node.left, node.right = node.right, node.left
            self.invertTree(node.left)
            self.invertTree(node.right)

    def invertTree(self, A):
        self.recursive_invert(A)
        return A
