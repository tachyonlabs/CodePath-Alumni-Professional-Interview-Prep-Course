# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        a_data = {}
        current = A
        while current:
            a_data[current] = 1
            current = current.next

        current = B
        while current:
            if current in a_data:
                return current
            current = current.next

        return None
