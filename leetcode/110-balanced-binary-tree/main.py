from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#
#        (4) 1
#           / \
#      (3) 2   2 (1)    left side height (4) is more than 1 time higher than the right side height (1)
#         / \
#    (2) 3   3
#       /
#  (1) 4
# Traverse depth first
# find the height of both the left and the right
# the height represented at the parent node should reflect the max height of the subtree
# for each node, check if the absolute value of the difference of the two is > 1 return -1
# time - O(n) where n is each node. We need to visit each node exactly once
# space - O(h) where h is the height of the tree. The solution is recursive which stacks calls as high as the tree
class Solution:

    def get_height(self, node: TreeNode) -> int:

        # once we reach a None
        if not node:
            return 0

        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)

        # If either subtree is unbalanced, propagate the failure (-1)
        if left_height == -1 or right_height == -1:
            return -1

        # base case
        if (abs(left_height-right_height)) > 1:
            return -1

        return max(left_height + 1, right_height + 1)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            if self.get_height(root) == -1:
                return False
            else:
                return True
        else:
            return True

def main():

    four_right = TreeNode(4)
    four_left = TreeNode(4)
    three_right = TreeNode(3)
    three_left = TreeNode(3)
    two_right = TreeNode(2)
    two_left = TreeNode(2)
    one = TreeNode(1)

    one.left=two_left
    one.right=two_right
    two_left.left=three_left
    two_right.right=three_right
    three_left.left=four_left
    three_left.right=four_right

    sol = Solution()
    print(sol.isBalanced(one))

if __name__ == "__main__":
    main()