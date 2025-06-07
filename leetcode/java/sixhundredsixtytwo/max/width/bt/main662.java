import sixhundredsixtytwo.max.width.bt.Solution;
import util.TreeNode;

/**
 * [1,3,2,5,null,null,9,6,null,7]
 *           1
 *          / \
 *         3   2
 *        /     \
 *       5       9
 *      /
 *     6       9
 *        /
 *       6
 *      /
 *     7
 */
public static void main() {
    Solution solution = new Solution();
    TreeNode nine = new TreeNode(9);
    TreeNode three = new TreeNode(3);
    TreeNode five = new TreeNode(5);
    TreeNode two = new TreeNode(2, null, nine);
    TreeNode three_ = new TreeNode(3, five, three);
    TreeNode one = new TreeNode(1, three_, two);
    println(solution.widthOfBinaryTree(one));
    println(solution.widthOfBinaryTree(new TreeNode(1)));
}