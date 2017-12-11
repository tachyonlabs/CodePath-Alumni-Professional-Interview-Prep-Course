# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param root : root node of tree
    # @param sum1 : integer
    # @return a list of list of integers
    def __init__(self):
        self.paths = []

    def traverse_sum(self, node, the_sum, path):
        if node:
            path += (node.val,)
            if not node.left and not node.right and sum(path) == the_sum:
                self.paths.append(list(path))
            self.traverse_sum(node.left, the_sum, path)
            self.traverse_sum(node.right, the_sum, path)

    def pathSum(self, root, sum1, path=tuple()):
        self.traverse_sum(root, sum1, tuple())
        return self.paths
