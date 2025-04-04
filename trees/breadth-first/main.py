from trees.Node import Node
from BreadthFirstTree import breadth_first_values

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
    #
    print(breadth_first_values(a))

if __name__ == "__main__":
    main()
