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
    // and now the stack version
    public ArrayList<Integer> preorderTraversal(TreeNode a) {
        ArrayList<Integer> preorder = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode node = a;
        while (stack.size() != 0 || node != null) {
            if (node != null) {
                preorder.add(node.val);
                stack.push(node);
                node = node.left;
            } else {
                node = stack.pop();
                node = node.right;
            }
        }
        return preorder;
    }
}
