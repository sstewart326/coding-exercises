package onehundred.same.tree;

import util.TreeNode;


public class Main {

    private static TreeNode getNode() {
        return new TreeNode(1, new TreeNode(2), new TreeNode(3));
    }

    public static void main() {
        Solution sol = new Solution();
        System.out.println(sol.isSameTree(getNode(), getNode()));
    }

}
