# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    # this is a super mess, I am definitely not at the top of my game today :-(
    def reverseBetween(self, A, m, n):
        if m == n or not A or not A.next:
            return A

        start = None
        count = 1
        mptr = A
        while count < m:
            start, mptr = mptr, mptr.next
            count += 1

        nptr, end = mptr, mptr.next
        while count < n:
            nptr, end = nptr.next, nptr.next.next
            count += 1

        prev = start
        current = mptr
        next = current.next
        while current.next != end:
            current.next = prev
            prev, current = current, next
            if current.next != end:
                next = current.next
            else:
                current.next = prev
                break

        mptr.next = end

        if m == 1:
            return current
        else:
            start.next = current
            return A
