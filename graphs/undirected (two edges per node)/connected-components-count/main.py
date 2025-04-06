from graphs.graph_util import convert_to_graph

def traverse_components_df(graph, node, visited):

    # check if node has been visited
    #   return if so
    #   else add node to visited

    # get neighbors of node via graph
    # recurse through those to fill out visited

    # at end, return visited

    if node in visited:
        return
    else:
        visited.add(node)

    neighbors = graph.get(node)
    for neighbor in neighbors:
        traverse_components_df(graph, neighbor, visited)

    return visited

def count_components(graph, visited):

    # iterate over nodes in graph
    # check if node is in visited
    #     if not, increment count and traverse
    #     else continue

    count = 0

    for n in graph:
        if n in visited:
            continue
        else:
            count += 1
            visited = traverse_components_df(graph, n, visited)

    return count


# time - O(e) where e is the edges
# space - O(n) where n is the nodes
def main():
    #        1--2
    #
    #         4
    #         |
    #      5--6--8
    #         |
    #         7
    #
    #         3
    graph = {
        3: [],
        4: [6],
        6: [4,5,7,8],
        8: [6],
        7: [6],
        5: [6],
        1: [2],
        2: [1]
    }
    print(count_components(graph, set()))

if __name__ == "__main__":
    main()