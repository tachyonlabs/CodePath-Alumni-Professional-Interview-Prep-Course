# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def get_max_path_sum(self, node):
        if not node:
            return 0

        left_max_sum_path = self.get_max_path_sum(node.left)
        right_max_sum_path = self.get_max_path_sum(node.right)

        max_with_one_or_no_child_paths = max(max(left_max_sum_path, right_max_sum_path) + node.val, node.val)
        max_with_both_child_paths = max(max_with_one_or_no_child_paths,
                                        left_max_sum_path + right_max_sum_path + node.val)
        self.max_sum_path = max(self.max_sum_path, max_with_both_child_paths)
        return max_with_one_or_no_child_paths

    def maxPathSum(self, A):
        self.max_sum_path = float("-inf")
        self.get_max_path_sum(A)
        return self.max_sum_path
