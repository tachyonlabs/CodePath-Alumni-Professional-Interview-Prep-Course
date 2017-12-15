/**
 * Definition for binary tree
 * class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) {
 *      val = x;
 *      left=null;
 *      right=null;
 *     }
 * }
 */
public class Solution {
    public void invert(TreeNode node) {
        if (node != null) {
            TreeNode temp = node.left;
            node.left = node.right;
            node.right = temp;
            invert(node.left);
            invert(node.right);
        }
    }
    public TreeNode invertTree(TreeNode A) {
        invert(A);
        return A;
    }
}
