from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#   find k smallest element in BST
#
#                                   10
#                                  /  \
#                                 5    11
#                                / \
#                               3   7
#                                \
#                                 4
#
#
#        what do we know?
#              traversing left until there is no more left is the smallest element
#              traversing right until there is no more right is the largest element
#
#       algo:
#           inorder traversal - left then check k then right
#
# time - O(h + k) where h is the height of the tree and k is the number of elements we need to back-traverse
# space - O(h) because the stack will have at most h nodes
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = 0
        return_val = None

        def traverse(node):
            if not node:
                return

            traverse(node.left)

            nonlocal count, return_val
            count += 1
            if count == k:
                return_val = node.val
                return

            traverse(node.right)

        traverse(root)
        return return_val

def main():
    four = TreeNode(4)
    three = TreeNode(3, None, four)
    seven = TreeNode(7)
    five = TreeNode(5, three, seven)
    eleven = TreeNode(11)
    ten = TreeNode(10, five,eleven)

    sol = Solution()
    print(sol.kthSmallest(ten, 4))


if __name__ == "__main__":
    main()