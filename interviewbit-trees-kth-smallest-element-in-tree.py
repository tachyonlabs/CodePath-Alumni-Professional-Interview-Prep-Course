# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root : root node of tree
    # @param k : integer
    # @return an integer
    def kthsmallest(self, root, k):
        """
        I decided to do an inorder traversal iteratively just because it would be very easy
        to keep track of a counter. At the point where you would normally print or store a
        node's data, I just increment the counter, and if it's equal to k, return node.val
        """
        stack = []
        counter = 0
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                counter += 1
                if counter == k:
                    return node.val

                node = node.right
