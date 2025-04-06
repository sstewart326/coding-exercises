def convert_to_graph(edges):
    # instantiate an empty graph
    # for each edge, check if graph contains the node
    # if it doesn't add to dictionary
    # else append the node to the array in the dictionary

    nodes = {}

    for edge in edges:
        start = edge[0]
        end = edge[1]
        if start in nodes:
            arr = nodes.get(start)
            arr.append(end)
        else:
            nodes[start] = [ end ]
        if end in nodes:
            arr = nodes.get(end)
            arr.append(start)
        else:
            nodes[end] = [ start ]

    return nodes

def find_shortest_path(graph, start, end):
    # start with a count 0
    # if start == end, return the count
    # else add start and count to the queue
    # while queue is not empty
    # pop(0) first added
    # if start == end, return the count
    # add all children to the queue with count + 1

    queue = [(start, 0)]
    visited = set()

    while queue:
        curr, count = queue.pop(0)
        if curr == end:
            return count

        if curr in visited:
            continue

        visited.add(curr)
        neighbors = graph.get(curr)
        for neighbor in neighbors:
            queue.append((neighbor, count+1))

    return -1

#
#   w--x--y--z
#   \       /      start=w
#    \__v__/       end=z
#                  ans = 3
def main():
    edges = [
        ['w', 'x'],
        ['x','y'],
        ['z','y'],
        ['z','v'],
        ['w','v']
    ]
    graph = convert_to_graph(edges)
    print(graph)
    print(find_shortest_path(graph, 'w', 'z')) # 2
    print(find_shortest_path(graph, 'w', 'x')) # 1
    print(find_shortest_path(graph, 'w', 'a')) # -1
    print(find_shortest_path(graph, 'w', 'w')) # 0





if __name__ == "__main__":
    main()