# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def start_dupes(self, head):
        return head and head.next and head.val == head.next.val

    def deleteDuplicates(self, A):
        # single-node list
        if not A.next:
            return A

        # list that starts with dupes
        while self.start_dupes(A):
            dupe_val = A.val
            while A and A.val == dupe_val:
                A = A.next

        # dupes not at the start
        current = A
        while current:
            while current.next and current.next.next and current.next.val == current.next.next.val:
                dupe_val = current.next.val
                next = current.next.next.next
                while next and next.val == dupe_val:
                    next = next.next
                current.next = next

            current = current.next

        return A
