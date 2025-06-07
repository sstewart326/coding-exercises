from typing import List


# time - O(n*m) size of the matrix
# space - O(n*m) size of the matrix
class Solution:

    # visited set
    # traverse until out of bounds or we reach a visited in the following order
    #    right -> down -> left -> up -> repeat
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        output = []

        def is_in_bounds(row, column):
            return 0 <= row < len(matrix) and 0 <= column < len(matrix[0])

        def traverse_right(row, column, matrix, visited):
            if is_in_bounds(row, column) and (row, column) not in visited:
                visited.add((row,column))
                output.append(matrix[row][column])
                return traverse_right(row, column + 1, matrix, visited)
            else:
                # we went out of bounds too far right so decrement column to move left
                # add 1 to row because the next move is down
                return row + 1, column - 1

        def traverse_down(row, column, matrix, visited):
            if is_in_bounds(row, column) and (row, column) not in visited:
                visited.add((row,column))
                output.append(matrix[row][column])
                return traverse_down(row + 1, column, matrix, visited)
            else:
                # we went out of bounds too far down so decrement row to move up
                # decrement 1 from the column because the next move is left
                return row - 1, column - 1

        def traverse_left(row, column, matrix, visited):
            if is_in_bounds(row, column) and (row, column) not in visited:
                visited.add((row,column))
                output.append(matrix[row][column])
                return traverse_left(row, column - 1, matrix, visited)
            else:
                # we went out of bounds too far left so increment column to move right
                # decrement 1 from the row because the next move is up
                return row - 1, column + 1

        def traverse_up(row, column, matrix, visited):
            if is_in_bounds(row, column) and (row, column) not in visited:
                visited.add((row,column))
                output.append(matrix[row][column])
                return traverse_up(row - 1, column, matrix, visited)
            else:
                # we went out of bounds too far up so increment the row to move down
                # add 1 to the column because the next move is right
                return row + 1, column + 1

        visited = set()
        r = 0
        c = 0
        while len(visited) < len(matrix) * len(matrix[0]):
            r, c = traverse_right(r, c, matrix, visited)
            r, c = traverse_down(r, c, matrix, visited)
            r, c = traverse_left(r, c, matrix, visited)
            r, c = traverse_up(r, c, matrix, visited)

        return output

def main():
    sol = Solution()
    # Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    #print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    print(sol.spiralOrder([[23,18,20,26,25],[24,22,3,4,4],[15,22,2,24,29],[18,15,23,28,28]]))

if __name__ == "__main__":
    main()