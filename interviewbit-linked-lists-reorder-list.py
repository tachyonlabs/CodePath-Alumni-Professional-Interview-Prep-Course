# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        if not A or not A.next or not A.next.next:
            return A

        """
        My simple three-pointers solution was correct, but got failed for not being 
        time-efficient enough :-( Let's try this one now ...
        """
        nodes_list = []
        current = A
        while current:
            nodes_list.append(current)
            current = current.next

        for i in range((len(nodes_list) - 1) / 2):
            print i, nodes_list[i].val
            temp = nodes_list[i].next
            nodes_list[i].next = nodes_list[-(i + 1)]
            nodes_list[-(i + 1)].next = temp
            nodes_list[-(i + 2)].next = None

        return A
