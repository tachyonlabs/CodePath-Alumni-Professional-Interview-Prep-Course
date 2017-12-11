# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def do_the_summing(self, node):
        if not node.left and not node.right:
            return node.val
        else:
            if node.left:
                node.left.val += node.val * 10
            if node.right:
                node.right.val += node.val * 10
            return (self.do_the_summing(node.left) if node.left else 0) + (self.do_the_summing(node.right) if node.right else 0)

    def sumNumbers(self, A):
        return self.do_the_summing(A) % 1003
