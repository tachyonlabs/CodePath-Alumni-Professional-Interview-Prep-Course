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
    def postorderTraversal(self, A):
        stack = []
        postorder = []
        node = A
        last_visited = None
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                stack_top_node = stack[-1]
                if stack_top_node.right and last_visited != stack_top_node.right:
                    node = stack_top_node.right
                else:
                    last_visited = stack.pop()
                    postorder.append(last_visited.val)

        return postorder
