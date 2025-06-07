package onehundredone.symetric.tree;

import util.TreeNode;

public class Solution {

    private boolean compareTrees(TreeNode tree1, TreeNode tree2) {
        if (tree1 == null && tree2 == null) {
            return true;
        }
        if (tree1 == null ^ tree2 == null) {
            return false;
        }
        if (tree1.val != tree2.val) {
            return false;
        }

        return compareTrees(tree1.left, tree2.right) && compareTrees(tree1.right, tree2.left);
    }

    public boolean isSymmetric(TreeNode root) {
        return compareTrees(root.left, root.right);
    }
}