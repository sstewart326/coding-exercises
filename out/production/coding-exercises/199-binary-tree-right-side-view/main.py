from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        if not root:
            return output

        queue = [ (0, root) ]
        level_tracker = []

        while queue:
            level, node = queue.pop(0)
            if level == len(level_tracker):
                level_tracker.append(node.val)
            else:
                level_tracker[level] = node.val

            if node.left:
                queue.append((level + 1, node.left))
            if node.right:
                queue.append((level + 1, node.right))

        return level_tracker

#              1
#             / \
#            2   3
#           /                1, 3, 4, 5
#          4
#           \
#            5
def main():
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)

    one.left = two
    one.right = three
    three.left = four
    four.left = six
    four.right = five

    sol = Solution()
    print(sol.rightSideView(one))


if __name__ == "__main__":
    main()