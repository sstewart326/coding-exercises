def bf(graph, start):

    traverse_queue = [ start ]

    while traverse_queue:
        curr = traverse_queue.pop(0)
        print(curr)
        for value in graph[curr]:
            traverse_queue.append(value)

def main():

    #  a->c->e
    #  ↓
    #  b
    #  ↓
    #  d->f
    graph = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
    }
    bf(graph, 'a') # a b c d e f

if __name__ == "__main__":
    main()