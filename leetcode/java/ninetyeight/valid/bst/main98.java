import ninetyeight.valid.bst.Solution;
import util.TreeNode;

public static void main() {
    Solution solution = new Solution();

    TreeNode three = new TreeNode(3);
    TreeNode six = new TreeNode(6);

    TreeNode four = new TreeNode(4, three, six);

    TreeNode one = new TreeNode(1);

    TreeNode five = new TreeNode(5, one, four);

    System.out.println(solution.isValidBST(five));
}
