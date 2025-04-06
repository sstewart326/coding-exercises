from graphs.graph_util import convert_to_graph


def path_exists_df(graph, src, dest, visited):

    # src == dest, return true
    # get neighbors in graph for src
    # mark the neighbor as visited
    # return end at false which signifies we never returned True



    if src == dest:
        return True
    if src in visited:
        return # stop the recursion
    else:
        visited.add(src)

    for neighbor in graph[src]:
        result = path_exists_df(graph, neighbor, dest, visited)
        if result:
            return result # we don't want to return if not true because we don't want to stop the recursion

    return False



#           i--j--k--l
#                 |
#                 m
#
#           o--n
#
def main():
    edges = [
        ['i', 'j'],
        ['k', 'i'],
        ['m', 'k'],
        ['k', 'l'],
        ['o', 'n']
    ]
    graph = convert_to_graph(edges)
    print(path_exists_df(graph, 'i', 'm', set()))
    print(path_exists_df(graph, 'i', 'o', set()))



if __name__ == "__main__":
    main()