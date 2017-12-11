# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        if not A or (not A.left and not A.right):
            return None

        stack = []
        node = A
        inorder = []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if inorder and inorder[-1] == B:
                    return node
                inorder.append(node.val)
                node = node.right

        return None
