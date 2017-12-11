# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    # "Using recursion is not allowed." -- Eek! It just feels wrong not to use recursion ...
    def inorderTraversal(self, A):
        stack = []
        in_order_values = []
        node = A
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                in_order_values.append(node.val)
                node = node.right

        return in_order_values
