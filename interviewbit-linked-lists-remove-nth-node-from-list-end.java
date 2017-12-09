/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
public class Solution {
    public ListNode removeNthFromEnd(ListNode a, int b) {
        int counter = 0;
        ListNode lead = a;
        ListNode follow = null;
        while (lead != null) {
            if (counter == b) {
                follow = a;
            }
            if (lead.next == null) {
                if (follow != null && follow.next != null) {
                    follow.next = follow.next.next;
                    return a;
                } else {
                    return a.next;
                }
            }
            lead = lead.next;
            counter += 1;
            if (follow != null) {
                follow = follow.next;
            }
        }
        return a.next;
    }
}
