from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# time - O(n * h) we visit each node once but need to copy when a node has both a left and right
# space - (n * h) recursion i h, previous_vals is h, total copies is n, aggregate array is n * h
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def traverse(node, curr_sum, previous_vals, aggregate):

            curr_sum += node.val
            previous_vals.append(node.val)

            # traverse
            if node.left and node.right:
                traverse(node.left, curr_sum, previous_vals, aggregate)
                traverse(node.right, curr_sum, previous_vals.copy(), aggregate)
            elif node.left:
                traverse(node.left, curr_sum, previous_vals, aggregate)
            elif node.right:
                traverse(node.right, curr_sum, previous_vals, aggregate)

            # we've reached leaf
            elif not node.left and not node.right and curr_sum == targetSum:
                aggregate.append(previous_vals)

            return aggregate

        if not root:
            return []
        return traverse(root, 0, [], [])

def main():
    sol = Solution()
    seven = TreeNode(7)
    two = TreeNode(2)
    five = TreeNode(5)
    one = TreeNode(1)
    eleven = TreeNode(11, seven, two)
    four = TreeNode(4, eleven)
    four_ = TreeNode(4, five, one)
    thirteen = TreeNode(13)
    eight = TreeNode(8, thirteen, four_)
    five_ = TreeNode(5, four, eight)
    #print(sol.pathSum(five_, 22))
    #print(sol.pathSum(TreeNode(-2, TreeNode(-3)), -5))
    #            1
    #           / \
    #         -2   -3
    #         / \    \
    #        1   3    -2
    #       /
    #      -1
    print(sol.pathSum(TreeNode(1, TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3)), TreeNode(-3, TreeNode(-2))), -1))

if __name__ == "__main__":
    main()
