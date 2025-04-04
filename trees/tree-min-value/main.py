from trees.Node import Node

# time complexity O(n) - we visit every node once
# space complexity O(n) - stack becomes of O(n) size
def depth_min(node, val):

    if not node:
        return val

    return min(node.value, depth_min(node.left, val), depth_min(node.right, val))

# time complexity O(n) - we visit every node once
# space complexity O(n) - nodes are pushed into a queue
def breadth_min(node):

    queue = [node]
    min_val = None

    while queue:
        curr = queue.pop(0)

        if not min_val:
            min_val = curr.value

        min_val = min(min_val, curr.value)

        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    return min_val

def main():
    a = Node(5)
    b = Node(3)
    c = Node(6)
    d = Node(10)
    e = Node(5)
    f = Node(7)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f


    #       5
    #      / \
    #     3   6
    #    / \   \
    #   10   5   7

    print("breadth sum", breadth_min(a))
    print("depth min", depth_min(a, a.value))



# Time Complexity - O(N) each node of the tree may be visited
# Space Complexity - O(N) nodes are stored in queue
if __name__ == "__main__":
    main()
