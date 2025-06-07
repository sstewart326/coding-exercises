import onehundredone.symetric.tree.Solution;
import util.TreeNode;

public static void main() {

    TreeNode r3 = new TreeNode(3);
    TreeNode r4 = new TreeNode(4);
    TreeNode r2 = new TreeNode(2, r4, r3);
    TreeNode l3 = new TreeNode(3);
    TreeNode l4 = new TreeNode(4);
    TreeNode l2 = new TreeNode(2, l3, l4);
    TreeNode root = new TreeNode(1, l2, r2);

    Solution sol = new Solution();
    println(sol.isSymmetric(root));
}