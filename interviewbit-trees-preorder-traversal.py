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
    def preorderTraversal(self, A):
        stack = []
        preorder_list = []
        node = A
        while node or stack:
            if node:
                preorder_list.append(node.val)
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node = node.right

        return preorder_list
