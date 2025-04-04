from trees.Node import Node

# time complexity O(n) - we visit every node once
# space complexity O(n) - stack becomes of O(n) size
def depth_max_root_leaf_sum(node):

    # algorithm:
    #   base case - we reach the leaf and take the value
    #   each iteration sums the largest value between the left and right child nodes

    if not node.left and not node.right:
        return node.value
    elif not node.left:
        return node.value + depth_max_root_leaf_sum(node.right)
    elif not node.right:
        return node.value + depth_max_root_leaf_sum(node.left)
    else:
        return node.value + max(depth_max_root_leaf_sum(node.left), depth_max_root_leaf_sum(node.right))

def main():
    a = Node(16)
    b = Node(3)
    c = Node(6)
    d = Node(15)
    e = Node(5)
    f = Node(8)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f


    #       5
    #      / \
    #     3   6
    #    / \   \
    #   15   16   8

    #print("breadth sum", breadth_min(a))
    print("depth max root to leaf", depth_max_root_leaf_sum(a))



# Time Complexity - O(N) each node of the tree may be visited
# Space Complexity - O(N) nodes are stored in queue
if __name__ == "__main__":
    main()
