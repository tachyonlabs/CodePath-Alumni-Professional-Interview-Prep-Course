
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        if not A or not A.next:
            return A

        head = A.next
        A.next = A.next.next
        head.next = A
        current = A
        while current.next and current.next.next:
            temp = current.next.next.next
            current.next, current.next.next = current.next.next, current.next
            current.next.next.next = temp
            current = current.next.next

        return head
