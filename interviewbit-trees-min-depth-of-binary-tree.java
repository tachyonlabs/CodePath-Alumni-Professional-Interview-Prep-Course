/**
 * Definition for binary tree
 * class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    class NodeAndDepth {
        TreeNode node;
        int depth;
        NodeAndDepth(TreeNode n, int d) {
            node = n;
            depth = d;
        }
    }
    public int minDepth(TreeNode a) {
        Queue<NodeAndDepth> queue = new LinkedList<NodeAndDepth>();
        queue.add(new NodeAndDepth(a, 1));
        NodeAndDepth nand;
        while (queue.size() != 0) {
            nand = queue.remove();
            if (nand.node.left == null && nand.node.right == null) {
                return nand.depth;
            } else {
                if (nand.node.left != null) {
                    queue.add(new NodeAndDepth(nand.node.left, nand.depth + 1));
                }
                if (nand.node.right != null) {
                    queue.add(new NodeAndDepth(nand.node.right, nand.depth + 1));
                }
            }
        }
        return 1;
    }
}
