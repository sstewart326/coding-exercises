from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# time - O(n) where n is the nodes in the tree
# space - O(n) due to the answer array holding n nodes
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [ [root] ]
        answer = []

        while queue:
            level = queue.pop(0)
            level_values = list(map(lambda node: node.val, level))
            answer.append(level_values)
            curr_level = []
            for node in level:
                if node.left:
                    curr_level.append(node.left)
                if node.right:
                    curr_level.append(node.right)
            if curr_level:
                queue.append(curr_level)

        return answer

#
#           3
#          / \
#         9   20          output = [[3], [9, 20], [15, 7]]
#            /  \
#           15   7
#
def main():
    three = TreeNode(3)
    nine = TreeNode(9)
    twenty = TreeNode(20)
    fifteen = TreeNode(15)
    seven = TreeNode(7)
    three.left = nine
    three.right = twenty
    twenty.left = fifteen
    twenty.right = seven

    sol = Solution()
    print(sol.levelOrder(three))

if __name__ == "__main__":
    main()