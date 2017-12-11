/**
 * Definition for binary tree
 * class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

// recursive first, then I'll redo it with a stack
public class Solution {
    public ArrayList<Integer> inorder = new ArrayList<Integer>();

    public ArrayList<Integer> inorderTraversal(TreeNode a) {
        traverse(a);
        return inorder;
    }
    public void traverse(TreeNode node) {
        if (node != null) {
            traverse(node.left);
            inorder.add(node.val);
            traverse(node.right);
        }
    }
}
