# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        length = 0
        current = A
        while current:
            length += 1
            current = current.next

        node_to_remove = max(length - B, 0)

        if node_to_remove == 0:
            return A.next

        current = A
        for i in range(length - B - 1):
            current = current.next

        current.next = current.next.next

        return A
