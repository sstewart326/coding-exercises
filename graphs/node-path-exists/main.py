def graph_contains_df(graph, character, target):

    # curr = graph[start]
    # curr contains end =)
    # else
    # recursively check all values from curr

    if character == target:
        return True

    for neighbor in graph[character]:
        has_path = graph_contains_df(graph, neighbor, target)
        if has_path:
            return True
        # we don't want to return if false because we don't want to stop the recursion

    return False

def graph_contains_bf(graph, character, target):

    # queue of the character
    # while queue
        # get neighbors via graph[character]
        # iterate neighbors
        # if neighbor = target return True
        # add neighbors of neighbor to the queue
    # return False, signifying no path has been found

    traversing_queue = [ character ]
    while traversing_queue:
        curr = traversing_queue.pop(0)
        if curr == target:
            return True
        for neighbor in graph[curr]:
            traversing_queue.append(neighbor)
    return False



def main():
    #      f-->g->h
    #      ↓   ^
    #   j->i---|
    #      ↓
    #      k
    graph = {
        'f': ['g', 'i'],
        'i': ['g', 'k'],
        'k': [],
        'g': ['h'],
        'h': [],
        'j': ['i']
    }
    print(graph_contains_df(graph, 'f', 'k'))
    print(graph_contains_df(graph, 'f', 'j'))
    print(graph_contains_bf(graph, 'f', 'k'))
    print(graph_contains_bf(graph, 'f', 'j'))




if __name__ == "__main__":
    main()