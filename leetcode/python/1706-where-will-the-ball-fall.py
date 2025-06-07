from typing import List

# [. 1,  1,  1, -1, -1]
# [. 1,  1,  1, -1, -1].      1 = right
# [ -1, -1, -1,  1,  1].      -1 = left
# [. 1,  1,  1,  1, -1].      falling either direction requires 2 neighboring coordinates in the same direction
# [ -1, -1, -1, -1, -1]]
#
#.   attempt to traverse 2 coordinates left or right
#.   drop into the bottom coordinate
#.   once we've reached oob at the bottom, record the answer
#
#.   edge case - if we are at extreme left or right of grid and direction leads to wall, set -1 for the answer
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def drop_ball(col):
            for row in range(len(grid)):
                direction = grid[row][col]
                next_col = col + direction

                # Check bounds and if ball gets stuck
                if (next_col < 0 or next_col >= len(grid[0]) or
                        grid[row][next_col] != direction):
                    return -1

                col = next_col
            return col

        return [drop_ball(col) for col in range(len(grid[0]))]

def main():
    sol = Solution()
    # [[1,1,1,1,1,1]
    # [-1,-1,-1,-1,-1,-1]
    # [1,1,1,1,1,1]
    # [-1,-1,-1,-1,-1,-1]]
    print(sol.findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))

if __name__ == "__main__":
    main()

