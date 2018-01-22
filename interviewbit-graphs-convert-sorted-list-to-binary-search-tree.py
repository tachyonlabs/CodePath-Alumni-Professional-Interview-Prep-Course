# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    def sortedListToBST(self, A):
        def add_node(tree_root, val):
            if val < tree_root.val:
                if not tree_root.left:
                    tree_root.left = TreeNode(val)
                else:
                    add_node(tree_root.left, val)
            else:
                if not tree_root.right:
                    tree_root.right = TreeNode(val)
                else:
                    add_node(tree_root.right, val)

        def pick_nums(low, high):
            if low <= high:
                med = (low + high) / 2
                add_node(root, vals[med])
                pick_nums(low, med - 1)
                pick_nums(med + 1, high)

        if not A:
            return None

        vals = []
        current = A
        while current:
            vals.append(current.val)
            current = current.next

        total_low = 0
        total_high = len(vals) - 1
        middle = total_high / 2
        root = TreeNode(vals[middle])
        pick_nums(total_low, middle - 1)
        pick_nums(middle + 1, total_high)

        return root
