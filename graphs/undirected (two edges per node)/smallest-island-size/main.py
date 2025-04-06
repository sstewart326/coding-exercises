import math


def get_size_of_land(world, row, column, visited):
    # if visited, out of bounds, or water return 0
    # else set count = 1 and append visited
    # traverse left to right, right to left, top to bottom, and bottom to top
    # each traversal should add to count

    if (row, column) in visited:
        return 0
    if row < 0 or row >= len(world):
        return 0
    if column < 0 or column >= len(world[0]):
        return 0
    visited.add((row, column))
    if world[row][column] == 0:
        return 0

    count = 1

    count += get_size_of_land(world, row + 1, column, visited)
    count += get_size_of_land(world, row - 1, column, visited)
    count += get_size_of_land(world, row, column + 1, visited)
    count += get_size_of_land(world, row, column - 1, visited)

    return count

def get_size_of_smallest_island(world):
    # init min_size, visited
    # iterate over each coordinate
    #   if ans we get back is > 0 and < min_size, set min_size
    # return min_size

    min_size = math.inf
    visited = set()

    for row in range(len(world)):
        for column in range(len(world[0])):
            curr_size = get_size_of_land(world, row, column, visited)
            if curr_size > 0 and curr_size < min_size:
                min_size = curr_size
    return min_size

def main():
    world = [
        [0,0,1,1,0,0],
        [1,0,1,1,0,0],   # smallest == 3
        [1,1,0,0,1,0],
        [0,1,0,0,1,1]
    ]
    print(get_size_of_smallest_island(world))


if __name__ == "__main__":
    main()