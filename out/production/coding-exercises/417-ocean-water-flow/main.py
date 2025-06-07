from typing import List

#        P
#   [1,2,2,3,5]
#   [3,2,3,4,4]              two traversals - one for pacific and one for atlantic
# P [2,4,5,3,1] A            each iteration check if last < curr, if so, mark the coord
#   [6,7,1,4,5]
#   [5,1,1,2,4]
#        A
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific_coords = set()
        atlantic_coords = set()


        def traverse(row, column, visited, previous, for_atlantic):
            if (row, column) in visited or not 0 <= row < len(heights) or not 0 <= column < len(heights[0]):
                return
            if for_atlantic:
                if (row, column) in atlantic_coords:
                    return
            else:
                if (row, column) in pacific_coords:
                    return

            visited.add((row, column))
            curr = heights[row][column]

            if curr >= previous:
                if for_atlantic:
                    atlantic_coords.add((row, column))
                else:
                    pacific_coords.add((row, column))
                for (r, c) in [(row+1, column),(row-1, column),(row, column+1),(row, column-1)]:
                    traverse(r, c, visited, curr, for_atlantic)

        # iterate for pacific
        for row in range(len(heights)):
            for column in range(len(heights[0])):
                if row == 0 or column == 0:
                    traverse(row, column, set(), -2**31, False)

        # iterate for atlantic
        for row in range(len(heights)):
            for column in range(len(heights[0])):
                if row == len(heights) - 1 or column == len(heights[0]) - 1:
                    traverse(row, column, set(), -2**31, True)

        return list(pacific_coords & atlantic_coords)

def main():
    sol = Solution()
    # print(sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
    # print(sol.pacificAtlantic([[1]]))

    # [3,3,3]
    # [3,1,3]
    # [0,2,4]
    print(sol.pacificAtlantic([[3,3,3],[3,1,3],[0,2,4]]))

if __name__ == "__main__":
    main()