/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode a, ListNode b) {
        if (a == null) {
            return b;
        }
        if (b == null) {
            return a;
        }
        ListNode aPtr = a;
        ListNode bPtr = b;
        ListNode newHead = new ListNode(0);
        ListNode current = newHead;
        int carry = 0;
        int total = 0;
        while (aPtr != null || bPtr != null || carry == 1) {
            total = carry;
            if (aPtr != null) {
                total += aPtr.val;
                aPtr = aPtr.next;
            }
            if (bPtr != null) {
                total += bPtr.val;
                bPtr = bPtr.next;
            }
            current.val = total % 10;
            carry = total / 10;
            if (aPtr != null || bPtr != null || carry == 1) {
                current.next = new ListNode(0);
                current = current.next;
            }
        }
        return newHead;
    }
}
