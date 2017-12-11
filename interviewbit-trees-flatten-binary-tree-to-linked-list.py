# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def __init__(self):
        self.preorder_vals = []

    def preorder(self, node):
        if node:
            self.preorder_vals.append(node.val)
            self.preorder(node.left)
            self.preorder(node.right)

    def flatten(self, A):
        if not A or (not A.left and not A.right):
            return A

        self.preorder(A)
        A.left = None
        current = A
        for val in self.preorder_vals[1:]:
            current.right = TreeNode(val)
            current = current.right

        return A
