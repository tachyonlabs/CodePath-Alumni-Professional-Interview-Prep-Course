/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode a, ListNode b) {
        if (a == null) {
            return b;
        } else if (b == null) {
            return a;
        }
        ListNode aPtr = a;
        ListNode bPtr = b;
        ListNode newHead;
        if (a.val <= b.val) {
            newHead = a;
            aPtr = a.next;
        } else {
            newHead = b;
            bPtr = b.next;
        }
        ListNode current = newHead;
        while (aPtr != null && bPtr != null) {
            if (aPtr.val <= bPtr.val) {
                current.next = aPtr;
                aPtr = aPtr.next;
            } else {
                current.next = bPtr;
                bPtr = bPtr.next;
            }
            current = current.next;
        }
        if (aPtr != null) {
            current.next = aPtr;
        } else if (bPtr != null) {
            current.next = bPtr;
        }
        return newHead;
    }
}
