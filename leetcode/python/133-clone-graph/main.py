class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

# time - O(v + e) each vertice (node) is visited once and each edge is traversed
# space - O(v) where v is the number of vertices (nodes)
class Solution:

    def copy(self, node: Node, old_to_new) -> Node:

        if node in old_to_new:
            return old_to_new[node]

        copy = Node(node.val)
        old_to_new[node] = copy

        for neighbor in node.neighbors:
            copy.neighbors.append(self.copy(neighbor, old_to_new))

        return old_to_new[node]



    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        return self.copy(node, {})



def main():
    sol = Solution()

    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    one.neighbors = [two, four]
    two.neighbors = [one, three]
    three.neighbors = [two, four]
    four.neighbors = [one, three]

    def print_node(node: Node):
        queue = [ node ]
        visited = set()

        while queue:
            n = queue.pop(0)

            if n in visited:
                continue
            else:
                visited.add(n)

            neighbors = []

            for neighbor in n.neighbors:
                neighbors.append(neighbor.val)
                queue.append(neighbor)

            print(neighbors)

    print_node(sol.cloneGraph(one))


if __name__ == "__main__":
    main()