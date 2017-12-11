/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
import java.util.ArrayDeque;

public class Solution {
    public static class TreeLinkNode {
        int val;
        TreeLinkNode left, right, next;
        TreeLinkNode(int x) { val = x; }
    }

    public static class QueueNodeInfo {
        TreeLinkNode node;
        int depth;
        QueueNodeInfo(TreeLinkNode n, int d) {
            node = n;
            depth = d;
        }
    }

    public static void main(String[] args) {
        TreeLinkNode[] nodes = new TreeLinkNode[8];
        for (int i = 1; i < 8; i ++) {
            nodes[i - 1] = new TreeLinkNode(i);
        }
        TreeLinkNode root = nodes[2];
        root.left = nodes[1];
        root.right = nodes[4];
        nodes[1].left = nodes[0];
        nodes[4].left = nodes[3];
        nodes[4].right = nodes[5];
        nodes[5].right = nodes[6];
        System.out.println("here");
        System.out.println(root.left.next);
        connect(root);
        System.out.println(root.left.next);
        System.out.println(root.left.next.val);
    }
    public static void connect(TreeLinkNode root) {
        if (root != null) {
            TreeLinkNode prev;
            int prevDepth;
            TreeLinkNode current = null;
            int depth = 0;
            ArrayDeque<QueueNodeInfo> queue = new ArrayDeque<>();
            queue.add(new QueueNodeInfo(root, 0));
            while (!queue.isEmpty()) {
                prev = current;
                prevDepth = depth;
                QueueNodeInfo currInfo = queue.remove();
                current = currInfo.node;
                depth = currInfo.depth;
                if (prev != null && prevDepth == depth) {
                    prev.next = current;
                }
                if (current.left != null) {
                    queue.add(new QueueNodeInfo(current.left, depth + 1));
                }
                if (current.right != null) {
                    queue.add(new QueueNodeInfo(current.right, depth + 1));
                }
            }
        }
    }
}
