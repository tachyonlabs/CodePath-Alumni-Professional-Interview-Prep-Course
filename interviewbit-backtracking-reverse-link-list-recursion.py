# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def __init__(self):
        self.head = None

    def recursive_reverse(self, node):
        if not node.next:
            self.head = node
            return
        else:
            self.recursive_reverse(node.next)
            temp = node.next
            temp.next = node
            node.next = None

    def reverseList(self, A):
        if not A or not A.next:
            return A

        self.recursive_reverse(A)
        return self.head
