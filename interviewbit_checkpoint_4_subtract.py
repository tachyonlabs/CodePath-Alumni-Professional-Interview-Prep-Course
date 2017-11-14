# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        if not A:
            return A

        node_vals = []

        current = A
        while current:
            node_vals.append(current.val)
            current = current.next

        current = A
        for i in range(len(node_vals) / 2):
            current.val = node_vals[len(node_vals) - i - 1] - current.val
            current = current.next

        return A
