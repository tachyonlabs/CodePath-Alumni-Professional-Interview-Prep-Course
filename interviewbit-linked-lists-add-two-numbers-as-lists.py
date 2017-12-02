# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        def get_len(head):
            length = 0
            current = head
            while current:
                length += 1
                current = current.next

            return length

        if not A:
            return B
        if not B:
            return A

        A_len, B_len = get_len(A), get_len(B)
        if B_len > A_len:
            A, B = B, A

        current_A, current_B = A, B
        carry = 0
        for i in range(max(A_len, B_len)):
            added = carry + current_A.val
            if current_B:
                added += current_B.val
                current_B = current_B.next
            current_A.val = added % 10
            carry = added / 10
            if current_A.next:
                current_A = current_A.next
            else:
                if carry:
                    current_A.next = ListNode(carry)

        return A
