class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# time - O(n) worst case we visit each node
# space - (h) where h is the height of the tree
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):
            if not node:
                return None
            if node == p or node == q:
                return node

            # traverse until we reach leaf or we find p or q
            left = dfs(node.left)
            right = dfs(node.right)

            # at this point we know either the current node is a forking point or
            # is a common ancestor including itself
            if left and right:
                return node
            else:
                return left if left else right

        return dfs(root)


#
#                 1
#                / \
#               2   3
#              /   / \
#             4   5   6
#
def main():
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)

    one.left = two
    one.right = three
    two.left = four
    three.left = five
    three.right = six

    sol = Solution()
    print(sol.lowestCommonAncestor(one, five, six).val)

if __name__ == "__main__":
    main()