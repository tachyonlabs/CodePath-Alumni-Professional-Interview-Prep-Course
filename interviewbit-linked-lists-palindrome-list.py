# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        if not A.next:
            return 1

        vals = [A.val]
        current = A.next
        while current:
            vals.append(current.val)
            current = current.next

        current = A
        for i in range(len(vals) / 2):
            if current.val != vals[-i - 1]:
                return 0
            current = current.next

        return 1
