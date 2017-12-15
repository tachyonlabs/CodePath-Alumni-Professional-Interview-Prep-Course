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
    public int hasPathSum(TreeNode A, int B) {
        if (A == null) {
            return 0;
        }
        if (A.left == null && A.right == null && A.val == B) {
            return 1;
        }
        return Math.min(1, hasPathSum(A.left, B - A.val) + hasPathSum(A.right, B - A.val));
    }
}
