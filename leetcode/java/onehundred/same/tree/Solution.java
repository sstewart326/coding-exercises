package onehundred.same.tree;

import util.TreeNode;

class Solution {

    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p != null && q != null) {
            if (p.val == q.val) {
                return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
            } else {
                return false;
            }
        } else {
            return p == null && q == null;
        }
    }
}
