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
    // first I'll do a recursion version, then a stack version
    public ArrayList<Integer> preorder = new ArrayList<Integer>();
    public void traverse(TreeNode node) {
        if (node != null) {
            preorder.add(node.val);
            traverse(node.left);
            traverse(node.right);
        }
    }
    public ArrayList<Integer> preorderTraversal(TreeNode a) {
        traverse(a);
        return preorder;
    }
}
