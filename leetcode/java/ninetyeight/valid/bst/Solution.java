package ninetyeight.valid.bst;

import util.TreeNode;

public class Solution {

    private boolean traverse(TreeNode node, long low, long high) {

        if (node == null) {
            return true;
        }

        if (node.val <= low || node.val >= high) {
            return false;
        }

        return traverse(node.left, low, node.val) && traverse(node.right, node.val, high);

    }

    public boolean isValidBST(TreeNode root) {
        return traverse(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
}