from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# time - O(n) where n is the number of nodes in the tree
# space - O(h) where h is the height of the tree
class Solution:

    def dfs_recurse(self, root: Optional[TreeNode]):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        entry = root, 1
        stack = [entry]
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            # right pushed first, so left will be popped (processed) first
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))

        return max_depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # return self.dfs_recurse(root)
        return self.dfs(root)


#           5
#          / \
#         3   6     max depth: 3
#              \
#               7
def main():
    sol = Solution()
    five = TreeNode(5)
    three = TreeNode(3)
    six = TreeNode(6)
    seven = TreeNode(7)
    five.left = three
    five.right = six
    six.right = seven
    print(sol.maxDepth(five))


if __name__ == "__main__":
    main()