# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BST:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data, node=None):
        # the following line is because you can't use instance variables
        # as class function defaults, so no node=self.head above
        node = node or self.head
        if not self.head:
            self.head = TreeNode(data)
        else:
            if data < node.val:
                if not node.left:
                    node.left = TreeNode(data)
                else:
                    self.insert(data, node.left)
            else:
                if not node.right:
                    node.right = TreeNode(data)
                else:
                    self.insert(data, node.right)


class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def recurse_array_to_bst(self, arr, bst, start, end):
        if start <= end:
            mid = (start + end) / 2
            bst.insert(arr[mid])
            self.recurse_array_to_bst(arr, bst, start, mid - 1)
            self.recurse_array_to_bst(arr, bst, mid + 1, end)

    def sortedArrayToBST(self, A):
        if not A:
            return None

        tree = BST()
        self.recurse_array_to_bst(A, tree, 0, len(A) - 1)
        return tree.head

