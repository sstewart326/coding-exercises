from typing import List



#   [0, 0, 0]                [0, 0, 0]
#   [0, 1, 0]     expected   [0, 1, 0]
#   [1, 1, 1]                [1, 1, 1]
#
class Solution:



    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if len(mat) <= 1:
            return [[0]]

        # BFS each coordinate, keeping track of the visited
        visited = {}

        return mat

def main():
    sol = Solution()
    # print(sol.updateMatrix([[0,0,0],[0,1,0],[0,0,0]])) # [[0,0,0],[0,1,0],[0,0,0]]
    print(sol.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])) # [[0,0,0],[0,1,0],[1,2,1]]
    # print(sol.updateMatrix([[0],[1]])) # [[0],[1]]

if __name__ == "__main__":
    main()