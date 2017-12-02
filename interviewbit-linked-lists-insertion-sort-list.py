# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        head_ptr = A
        tail_ptr = A
        while tail_ptr.next:
            if tail_ptr.next.val < tail_ptr.val:
                temp = tail_ptr.next
                tail_ptr.next = tail_ptr.next.next
                if temp.val < head_ptr.val:
                    temp.next = head_ptr
                    head_ptr = temp
                else:
                    current = head_ptr
                    while current.next.val < temp.val:
                        current = current.next
                    current.next, temp.next = temp, current.next
            else:
                tail_ptr = tail_ptr.next

        return head_ptr
