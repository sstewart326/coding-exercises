from trees.Node import Node

def target_exists_breadth(root, target):

    # not required. just to print debug
    values = []

    # queue for each node we visit
    queue = [root]

    while queue:
        # pop the head of the queue
        node = queue.pop(0)
        # and add it to the values
        values.append(node.value)

        if node.value == target:
            print("processed ", values)
            return True

        # if the node has children, add them to the queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return False

def target_exists_depth(root, target):

    if root is None:
        return False

    print("processing ", root.value)

    if root.value == target:
        return True

    # if our target is in one of the nodes, one of the nodes
    # will return true and this logical or will return true
    return target_exists_depth(root.left, target) or target_exists_depth(root.right, target)

def main():
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       a
    #      / \
    #     b   c
    #    / \   \
    #   d   e   f

    # breadth is a much easier solution
    print(target_exists_breadth(a, 'D')) # true
    print(target_exists_breadth(a, 'G')) # false

    # depth is more difficult in a recursive type implementation
    print(target_exists_depth(a, 'D')) # true
    print(target_exists_depth(a, 'G')) # false

# Time Complexity - O(N) each node of the tree may be visited
# Space Complexity - O(N) nodes are stored in queue
if __name__ == "__main__":
    main()
