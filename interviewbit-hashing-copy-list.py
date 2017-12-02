# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        copy_head = RandomListNode(head.label)
        current, copy_current = head, copy_head
        copy_nodes = {}
        while current.next:
            copy_nodes[copy_current.label] = copy_current
            new_copy = RandomListNode(current.next.label)
            copy_current.next = new_copy
            current, copy_current = current.next, copy_current.next

        copy_nodes[copy_current.label] = copy_current
        current, copy_current = head, copy_head
        while current:
            if current.random:
                copy_current.random = copy_nodes[current.random.label]
            current, copy_current = current.next, copy_current.next

        return copy_head
