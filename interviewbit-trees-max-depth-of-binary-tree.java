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
    public int maxDepth(TreeNode a) {
        if (a == null) {
            return 0;
        } else if (a.left == null && a.right == null) {
            return 1;
        } else {
            return Math.max(maxDepth(a.left) + 1, maxDepth(a.right) + 1);
        }
    }
}
