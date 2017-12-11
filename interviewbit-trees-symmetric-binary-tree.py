# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def __init__(self):
        self.inorder_vals = []

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.inorder_vals.append(node.val)
            self.inorder(node.right)

    def isSymmetric(self, A):
        self.inorder_vals = []
        self.inorder(A)
        return 1 if self.inorder_vals == self.inorder_vals[::-1] else 0
