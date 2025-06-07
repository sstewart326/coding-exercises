class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
#        6
#       /  \
#      /    \        p=3      p=2          p=2           p=2
#     2      8       q=9      q=8          q=4           q=1 (doesn't exit)
#    / \    / \      lca=6    lca=6        lca=2         lca=2
#   0   4   7  9
#      / \
#     3   5
# because this is a binary tree we can assume the following
#   if p or q is less than curr node and the other p or q is greater than curr node, we are at the lca
#   else traverse left if both numbers are less than node
#        traverse right if both numbers are greater than node
#   if curr node equals p or q, return curr node
# runtime - O(h) - h is the height of the tree. We visit a max h nodes
# space - O(h) - h is the height of the tree. we are stacking calls since this is recursive
class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val > root.val:
            return root
        elif p.val > root.val and q.val < root.val:
            return root
        elif p.val == root.val or q.val == root.val:
            return root
        elif p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)


def main():
    sol = Solution()

    five = TreeNode(5)
    three = TreeNode(3)
    nine = TreeNode(9)
    seven = TreeNode(7)
    four = TreeNode(4)
    four.left = three
    four.right = five
    zero = TreeNode(0)
    eight = TreeNode(8)
    eight.left = seven
    eight.right = nine
    two = TreeNode(2)
    two.left = zero
    two.right = four
    six = TreeNode(6)
    six.left = two
    six.right = eight

    p = two
    q = eight
    print(sol.lowestCommonAncestor(six, p, q).val) # 6

    p = four
    q = three
    print(sol.lowestCommonAncestor(six, p, q).val) # 4

    p = seven
    q = nine
    print(sol.lowestCommonAncestor(six, p, q).val) # 8

if __name__ == "__main__":
    main()