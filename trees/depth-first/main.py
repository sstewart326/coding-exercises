from trees.Node import Node
from DepthFirstTree import traverse

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
    traverse(a)

if __name__ == "__main__":
    print("hi")
    main()
