from typing import Optional, NewType


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#          1                                                       1  diam = 4, h = 3
#         / \                                                       \
# (3)    2   4  (1)        diameter = 4                              2  diam = 4, h = 2
#       / \                                                         / \
# (2)  5   3 (1)                                  diam = 1 h = 1   3   4 diam = 1 h = 1
#     /                                                           /     \
#(1) 6                                      diam = 0 height = 0  5       6 diam = 0 height = 0
#
#
# need to track two things
#   height: max(left, right)
#   diameter: left + right + 1 (to account for our current node)
# when we reach a leaf, return 1
# diameter formula - left_height + right_height
# height formula - max(left_height, right_height)

# time - O(n) where n is each node
# space - O(n) for a completely unbalanced tree. O(logn) for a balanced tree. This is due to
#         the stack recursion
class Solution:

    Height = NewType('height', int)
    Diameter = NewType('diameter', int)

    def recurse(self, node) -> (Height, Diameter):
        if not node:
            return 0, 0
        if not node.left and not node.right:
            return 1, 1

        left_height, left_diameter = self.recurse(node.left)
        right_height, right_diameter = self.recurse(node.right)

        # diameter is taking max of heights and diameters because already calculated diameters could
        # be taller than the current left_height + right_height
        return max(left_height, right_height) + 1, max(left_height + right_height, right_diameter, left_diameter)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right):
            return 0
        return self.recurse(root)[1]



#          1                                                       1  diam = 4, h = 3
#         / \                                                       \
# (3)    2   4  (1)        diameter = 4                              2  diam = 4, h = 2    diameter = 4
#       / \                                                         / \
# (2)  5   3 (1)                                  diam = 1 h = 1   3   4 diam = 1 h = 1
#     /                                                           /     \
#(1) 6                                      diam = 0 height = 0  5       6 diam = 0 height = 0
#
#
# need to track two things
#   height: max(left, right)
#   diameter: left + right + 1 (to account for our current node)
# when we reach a leaf, return 1
def main():
    sol = Solution()
    one = TreeNode(1)
    two= TreeNode(2)
    five = TreeNode(5)
    three = TreeNode(3)
    four = TreeNode(4)
    six = TreeNode(6)

    one.left = two
    one.right = four
    two.left = five
    two.right = three
    five.left = six
    print(sol.diameterOfBinaryTree(one))


    one = TreeNode(1)
    two= TreeNode(2)
    five = TreeNode(5)
    three = TreeNode(3)
    four = TreeNode(4)
    six = TreeNode(6)
    one.right = two
    two.right = four
    four.right = six
    two.left = three
    three.left = five
    print((sol.diameterOfBinaryTree(one)))

if __name__ == "__main__":
    main()