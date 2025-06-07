import math
from typing import List



#   [0, 0, 0]                [0, 0, 0]
#   [0, 1, 0]     expected   [0, 1, 0]
#   [1, 1, 1]                [1, 2, 1]
#
#   time - (r * c)
#   space - (r * c * 2) for processing_queue and mat_copy
class Solution:



    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        # indexes to process, start at 0's
        processing_queue = []
        mat_copy = [[math.inf for _ in range(len(mat[0]))] for _ in range(len(mat))]

        # set 1's to infinity since each coordinate will be a count and we are trying to find min distance
        # to 0 and infinity will always be greater than distance to 0 before we update
        for row in range(len(mat)):
            for column in range(len(mat[0])):
                if mat[row][column] == 0:
                    mat_copy[row][column] = 0
                    processing_queue.append((row, column))

        def set_neighbor_count(r, c, dist_from_0):
            if r < 0 or r >= len(mat) or c < 0 or c >= len(mat[0]):
                return

            if dist_from_0 < mat_copy[r][c]:
                mat_copy[r][c] = dist_from_0
                processing_queue.append((r, c))

        while processing_queue:
            r, c = processing_queue.pop(0)
            set_neighbor_count(r - 1, c, 1 + mat_copy[r][c])
            set_neighbor_count(r + 1, c, 1 + mat_copy[r][c])
            set_neighbor_count(r, c - 1, 1 + mat_copy[r][c])
            set_neighbor_count(r, c + 1, 1 + mat_copy[r][c])

        return mat_copy



def main():
    sol = Solution()
    #print(sol.updateMatrix([[0,0,0],[0,1,0],[0,0,0]])) # [[0,0,0],[0,1,0],[0,0,0]]
    #print(sol.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])) # [[0,0,0],[0,1,0],[1,2,1]]
    print(sol.updateMatrix([[0],[1]])) # [[0],[1]]

if __name__ == "__main__":
    main()