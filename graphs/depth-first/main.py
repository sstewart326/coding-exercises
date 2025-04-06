def df(graph, start):
    print(start)
    if start not in graph:
        return

    vals = graph[start]
    for v in vals:
        df(graph, v)

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
    df(graph, 'a') # a,b,d,f,c,e

if __name__ == "__main__":
    main()