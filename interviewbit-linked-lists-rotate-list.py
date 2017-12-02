# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        if not A or not A.next:
            return A

        length = 0
        current = A
        while current:
            length += 1
            last = current
            current = current.next

        B %= length
        if B != 0:
            i = length - 1
            current = A
            while i > B:
                current = current.next
                i -= 1

            old_head = A
            A = current.next
            current.next = None
            last.next = old_head

        return A
