def is_island(world, row, column, visited):
    # return false
    #    if we found water
    #    if we are out of bounds
    #    if we reached an already explored area
    # else
    #    depth search left to right, right to left, top to bottom, bottom to top

    if (row, column) in visited:
        return False
    if row < 0 or row >= len(world):
        return False
    if column < 0 or column >= len(world[0]):
        return False
    if world[row][column] == 0:
        visited.add((row, column))
        return False

    visited.add((row, column))

    is_island(world, row-1, column, visited)
    is_island(world, row+1, column, visited)
    is_island(world, row, column-1, visited)
    is_island(world, row, column+1, visited)

    # we explored an island and traversed all possible directions
    return True



def count_islands(world):
    # island_count = 0
    # visited = set()
    # iterate over entire graph
    # if we find unvisited land, increment island_count and initiate a depth first traversal

    island_count = 0
    visited = set()

    for row in range(len(world)):
        for column in range(len(world[0])):
            if (is_island(world, row, column, visited)):
                island_count += 1

    return island_count


def main():
    world = [
        [0,0,1,1,0,0],
        [1,0,1,1,0,0],   # three islands
        [1,1,0,0,0,0],
        [0,0,0,0,0,1]
    ]
    print(count_islands(world))

if __name__ == "__main__":
    main()