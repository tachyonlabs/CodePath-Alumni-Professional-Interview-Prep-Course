# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if not A:
            return B
        if not B:
            return A

        ptrA, ptrB = A, B

        if A.val <= B.val:
            new_head = A
            ptrA = A.next
        else:
            new_head = B
            ptrB = B.next

        current = new_head
        while ptrA and ptrB:
            if ptrA.val <= ptrB.val:
                current.next = ptrA
                current = ptrA
                ptrA = ptrA.next
            else:
                current.next = ptrB
                current = ptrB
                ptrB = ptrB.next

        if ptrA:
            current.next = ptrA
        if ptrB:
            current.next = ptrB

        return new_head
