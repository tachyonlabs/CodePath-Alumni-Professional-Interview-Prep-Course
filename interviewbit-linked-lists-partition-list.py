# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        # my in-place solution was getting failed for not being efficient enough, so let's try this:
        if not A or not A.next:
            return A

        l_nodes_head = None
        l_nodes_tail = None
        ge_nodes_head = None
        ge_nodes_tail = None

        current = A
        while current:
            if current.val < B:
                if not l_nodes_head:
                    l_nodes_head = current
                    l_nodes_tail = current
                else:
                    l_nodes_tail.next = current
                    l_nodes_tail = l_nodes_tail.next
            else:
                if not ge_nodes_head:
                    ge_nodes_head = current
                    ge_nodes_tail = current
                else:
                    ge_nodes_tail.next = current
                    ge_nodes_tail = ge_nodes_tail.next

            current = current.next

        if ge_nodes_head:
            ge_nodes_tail.next = None

        if l_nodes_head:
            l_nodes_tail.next = ge_nodes_head
            return l_nodes_head
        else:
            return ge_nodes_head
