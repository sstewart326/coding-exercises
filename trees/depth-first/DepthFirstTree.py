# uses stack by default since the implementation is recursive
def traverse(node):

    if not node:
        return

    print(node.value)
    # node.val for preorder
    traverse(node.left)
    # node.val for inorder
    traverse(node.right)
    # node.val for postorder
