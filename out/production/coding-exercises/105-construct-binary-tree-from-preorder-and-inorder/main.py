from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#
# preorder always starts at the root
# inorder tells us what is on the left and right side of the root
#
# preorder = [3,9,20,15,7]
# this tell us the root is 3
#
# inorder = [9,3,15,20,7]
# this tells us we have one branch on the left of root and three on the right
#
# from root 3 inorder shows:
# left = [9] right = [15,20,7]
#
# from root 15 inorder shows:
# left = [] right = [20,7]

class Solution:

    # Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    # Output: [3,9,20,null,null,15,7]
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) > 0:
            root = TreeNode(preorder[0])
            mid_index = inorder.index(preorder[0])
            left_subtree = inorder[:mid_index]
            right_subtree = inorder[mid_index + 1:]

            root.left = self.buildTree(preorder[1:mid_index + 1],left_subtree)
            root.right = self.buildTree(preorder[mid_index + 1:],right_subtree)

            return root

        return None

def main():
    sol = Solution()
    tree = sol.buildTree([3,9,20,15,7], [9,3,15,20,7])

    queue = [ tree ]
    while queue:
        node = queue.pop(0)
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


if __name__ == "__main__":
    main()