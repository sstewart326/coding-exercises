from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # add rotten oranges to a queue as these will be our starts
        # determine the number of non-rotten oranges

        # traverse neighbors of each item in the queue
        # dequeue all items in the queue for each iteration and increment the minutes at the end
        # if non-rotten orange, mark it as rotten and queue the position

        # at the end, if we have 0 fresh oranges left, return the minutes -1 (to account for final step where we dequeue oranges at the edges of the graph)
        # else return -1

        FRESH_ORANGE = 1
        ROTTEN_ORANGE = 2

        queue = []
        num_of_min = 0
        num_of_fresh_oranges = 0

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == FRESH_ORANGE:
                    num_of_fresh_oranges += 1
                elif grid[row][column] == ROTTEN_ORANGE:
                    queue.append((row, column))
        if num_of_fresh_oranges == 0:
            return 0

        while queue:
            # pop each orange from the queue
            # get all orange neighbors and mark them as rotten
            # append them to the queue and increment the minute
            for _ in range(len(queue)):
                row, column = queue.pop(0)

                for (next_row, next_column) in [(row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)]:
                    if 0 <= next_row < len(grid) and 0 <= next_column < len(grid[0]) and grid[next_row][next_column] == FRESH_ORANGE:
                        # mark as ROTTEN so we don't revisit
                        grid[next_row][next_column] = ROTTEN_ORANGE
                        num_of_fresh_oranges -= 1
                        queue.append((next_row, next_column))
            num_of_min += 1
        # account for the last step where we dequeue the last orange but have nowhere else to traverse to
        num_of_min -= 1

        if num_of_fresh_oranges > 0:
            return -1
        else:
            return num_of_min



def main():
    sol = Solution()

    # [2,1,1]
    # [1,1,0]
    # [0,1,1]
    print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) # 4
    print(sol.orangesRotting([[0,2]])) # 0
    print(sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])) # -1
    # [2,1,1]
    # [1,0,2]
    # [0,1,1]
    # [0,1,0]
    print(sol.orangesRotting([[2,1,1],[1,0,2],[0,1,1],[0,1,0]]))

if __name__ == "__main__":
    main()