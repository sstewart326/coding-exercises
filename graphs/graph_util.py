def convert_to_graph(edges):

    # iterate over all edges
    # each edge has two nodes
    #

    graph = {}
    for edge in edges:
        [node1, node2] = edge
        if node1 not in graph:
            graph[node1] = [ node2 ]
        else:
            graph.get(node1).append(node2)
        if node2 not in graph:
            graph[node2] = [ node1 ]
        else:
            graph.get(node2).append(node1)
    return graph