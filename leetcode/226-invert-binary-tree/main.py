# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# runtime - O(n) - we traverse each node
# space - O(w) - w is the width of the tree (aka max size of the traversing queue)
class Solution:


    #         4
    #       /   \
    #      2     7
    #     / \   / \
    #    1   3 6   9

    # Output
    # [4,2,7,1,3,6,9]
    # Expected
    # [4,7,2,9,6,3,1]
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        traversing_queue = [ root ]

        while traversing_queue:
            node = traversing_queue.pop(0)
            if node.right:
                # push the right node into queue first so it gets processed first
                traversing_queue.append(node.right)
            if node.left:
                traversing_queue.append(node.left)
            # swap left and right values
            left = node.left
            right = node.right
            node.left = right
            node.right = left

        return root


def main():
    sol = Solution()

    left2 = TreeNode(6)
    right2 = TreeNode(9)

    left1 = TreeNode(1)
    right1 = TreeNode(3)

    left0 = TreeNode(2, left1, right1)
    right0 = TreeNode(7, left2, right2)
    root = TreeNode(4, left0, right0)


    # input = [4,2,7,1,3,6,9]
    #         4
    #       /   \
    #      2     7
    #     / \   / \
    #    1   3 6   9

    ans = sol.invertTree(root)
    ans_queue = [ ans ]
    while ans_queue:
        val = ans_queue.pop()
        print(val.val)
        if val.left:
            ans_queue.append(val.left)
        if val.right:
            ans_queue.append(val.right)

if __name__ == "__main__":
    main()