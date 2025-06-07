from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def explore_island(row, column, visited):
            if (row, column) in visited:
                return False
            if row < 0 or row == len(grid):
                return False
            if column < 0 or column == len(grid[0]):
                return False

            visited.add((row, column))
            if grid[row][column] == '0':
                return False

            explore_island(row + 1, column, visited)
            explore_island(row - 1, column, visited)
            explore_island(row, column + 1, visited)
            explore_island(row, column - 1, visited)

            return True

        islands = 0
        visited = set()
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if explore_island(row, column, visited):
                    islands += 1

        return islands


def main():
    sol = Solution()
    print(sol.numIslands([]))
    print(sol.numIslands([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]))
    print(sol.numIslands([
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]))

if __name__ == "__main__":
    main()