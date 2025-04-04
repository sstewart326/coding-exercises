# we can't recurse because recursion creates a stack implementation
# and breadth first relies on queues (FIFO)
def breadth_first_values(node):
    if not node:
        return

    # return array
    values = []

    # nodes get placed in the queue as we traverse
    queue = [node]

    while len(queue) > 0:

        # remove head element from queue
        current = queue.pop(0)
        # and append it to the values array
        values.append(current.value)

        # if the node has left or right children, add them to the queue
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return values