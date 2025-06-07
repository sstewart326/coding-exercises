from typing import List


class Solution:

    def flip_colors_bfs(self, image, row, column, starting_color, new_color, visited):

        queue = [ (row, column) ]

        while queue:
            row, column = queue.pop(0)

            if (row, column) in visited:
                continue
            if row < 0 or row >= len(image):
                continue
            if column < 0 or column >= len(image[0]):
                continue
            if image[row][column] != starting_color:
                visited.add((row, column))
                continue

            visited.add((row, column))
            image[row][column] = new_color

            queue.append((row + 1, column))
            queue.append((row - 1, column))
            queue.append((row, column + 1))
            queue.append((row, column - 1))

        return image

    def flood_fill_stack(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_color = image[sr][sc]
        if starting_color == color:
            return image
        return self.flip_colors_bfs(image, sr, sc, starting_color, color, set())



    # depth first solution
    # time - O(n) - n is the number of nodes in the image
    # space - O(n) - n is the number of nodes in the image
    #         worst case is we only have one row of colors that need to be changed
    def flip_colors(self, image, row, column, starting_color, new_color, visited):

        # if row, column has been visited, return
        # if row, column is out of bounds, return
        # add row, column to visited
        # if image[row][column] != starting_color return

        # add row, column to visited
        # set image[row][column] = new_color
        # return image

        if (row, column) in visited:
            return
        if row < 0 or row >= len(image):
            return
        if column < 0 or column >= len(image[0]):
            return
        if image[row][column] != starting_color:
            return

        visited.add((row, column))
        image[row][column] = new_color

        self.flip_colors(image, row + 1, column, starting_color, new_color, visited)
        self.flip_colors(image, row - 1, column, starting_color, new_color, visited)
        self.flip_colors(image, row, column + 1, starting_color, new_color, visited)
        self.flip_colors(image, row, column - 1, starting_color, new_color, visited)

        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_color = image[sr][sc]
        if starting_color == color:
            return image
        return self.flip_colors(image, sr, sc, starting_color, color, set())



def main():
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    new_color = 2

    sol = Solution()
    for row in sol.floodFill(image, sr, sc, new_color):
        print(row)
    print()
    for row in sol.flood_fill_stack(image, sr, sc, new_color):
        print(row)

    print()

    image = [[0,0,0],[0,0,0]]
    sr = 1
    sc = 0
    new_color = 2
    for row in sol.floodFill(image, sr, sc, new_color):
        print(row)
    print()
    for row in sol.flood_fill_stack(image, sr, sc, new_color):
        print(row)





if __name__ == "__main__":
    main()