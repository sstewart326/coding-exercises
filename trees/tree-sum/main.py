from trees.Node import Node

# time complexity O(n) - we visit every node once
# space complexity O(n) - stack becomes of O(n) size
def depth_sum(node, sum):

    if not node:
        return sum

    return node.value + depth_sum(node.left, sum) + depth_sum(node.right, sum)

# time complexity O(n) - we visit every node once
# space complexity O(n) - nodes are pushed into a queue
def breadth_sum(node):

    sum = 0

    queue = [node]
    while queue:
        n = queue.pop(0)
        sum += n.value

        if n.left:
            queue.append(n.left)
        if n.right:
            queue.append(n.right)

    return sum


def main():
    a = Node(5)
    b = Node(3)
    c = Node(6)
    d = Node(2)
    e = Node(4)
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
    #   2   4   7

    print("breadth sum", breadth_sum(a))
    print("depth sum", depth_sum(a, 0))



# Time Complexity - O(N) each node of the tree may be visited
# Space Complexity - O(N) nodes are stored in queue
if __name__ == "__main__":
    main()
