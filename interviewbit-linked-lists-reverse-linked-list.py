# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        current = A
        temp = None
        while True:
            next = current.next
            temp, current.next = current, temp
            if next:
                current = next
            else:
                return current
