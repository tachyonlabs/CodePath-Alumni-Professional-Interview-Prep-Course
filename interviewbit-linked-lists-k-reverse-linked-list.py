# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    # Alas, I kept screwing up my more elegant solution :-(
    def reverse_bucket(self, head):
        current = head
        temp = None
        while True:
            next = current.next
            temp, current.next = current, temp
            if next:
                current = next
            else:
                return current

    def reverseList(self, A, B):
        if not A or not A.next or B == 1:
            return A

        buckets = []
        bucket_head = A
        current = A
        count = 0
        while current:
            count += 1
            if count % B == 0:
                old_bucket_head = bucket_head
                bucket_head = current.next
                current.next = None
                current = bucket_head
                buckets.append(self.reverse_bucket(old_bucket_head))
            else:
                current = current.next

        new_head = buckets[0]

        for i, bucket in enumerate(buckets[:-1]):
            current = bucket
            while current.next:
                current = current.next

            current.next = buckets[i + 1]

        return new_head
