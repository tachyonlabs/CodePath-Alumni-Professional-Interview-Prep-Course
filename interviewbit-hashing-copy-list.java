/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        HashMap<Integer, RandomListNode> nodes = new HashMap<Integer, RandomListNode>();
        RandomListNode copyHead = new RandomListNode(head.label);
        nodes.put(copyHead.label, copyHead);
        RandomListNode current = head;
        RandomListNode currentCopy = copyHead;
        while (current.next != null) {
            currentCopy.next = new RandomListNode(current.next.label);
            currentCopy = currentCopy.next;
            nodes.put(currentCopy.label, currentCopy);
            current = current.next;
        }
        current = head;
        currentCopy = copyHead;
        while (current != null) {
            if (current.random != null) {
                currentCopy.random = nodes.get(current.random.label);
            }
            current = current.next;
            currentCopy = currentCopy.next;
        }
        return copyHead;
    }
}
