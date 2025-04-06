def traverse(graph, node, visited):

    # if node in visited, return 0
    # else set size to 1
    # recurse over neighbors and sum size
    # return size

    if node in visited:
        return 0

    visited.add(node)

    count = 1

    neighbors = graph.get(node)
    for neighbor in neighbors:
        count += traverse(graph, neighbor, visited)

    return count


def iterate(graph):
    # keep track of highest_count
    # initiate visited to {}
    # iterate over each node of the graph
    # if the node is in visited, skip
    # else traverse and see if we need to set the highest_count
    # return the highest_count
    highest_count = 0
    visited = set()

    for node in graph:
        if node in visited:
            continue
        else:
            count = traverse(graph, node, visited)
            if count > highest_count:
                highest_count = count

    return highest_count

# time - O(e) where e is the edges
# space - O(n) where n is the nodes
def main():
    #
    #   1--0--8
    #       \/
    #        5
    #
    #    4--2
    #     \/
    #      3
    #
    #    largest = 4
    graph = {
        0:[8,1,5],
        1:[0],
        5:[0,8],
        8:[0,5],
        2:[3,4],
        3:[2,4],
        4:[3,2]
    }
    print(iterate(graph))

if __name__ == "__main__":
    main()