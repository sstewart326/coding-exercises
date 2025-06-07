from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# time - O(n) where n is the number of nodes
# space - O(n) n the number of nodes which is the worst case stack size
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def is_valid(node, minn, maxx):

            if not node:
                return True

            if not minn < node.val < maxx:
                return False

            if not is_valid(node.left, minn, node.val) or not is_valid(node.right, node.val, maxx):
                return False

            return True

        return is_valid(root, float("-inf"), float("inf"))


def main():
    sol = Solution()

    #               3
    #              / \
    #             2   5
    #                  \
    #                   6
    three = TreeNode(3)
    two = TreeNode(2)
    five = TreeNode(5)
    one = TreeNode(1)
    six = TreeNode(6)
    three.left = two
    three.right = five
    five.right = six
    #five.left = one
    print(sol.isValidBST(three))


if __name__ == "__main__":
    main()