import math
from typing import List


class Solution:

    def generate_map(self, edges: List[List[int]]):
        dict = {}
        for x,y in edges:
            x_neighbors = dict.get(x, [])
            y_neighbors = dict.get(y, [])

            x_neighbors.append(y)
            y_neighbors.append(x)

            dict[x] = x_neighbors
            dict[y] = y_neighbors

        return dict


    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = self.generate_map(edges)

        # from bottom up, calculate distance from leaf nodes
        # leaf nodes == nodes with one edge
        # distance is the max height of all paths

        height_dictionary = {}

        def calculate_height(vertex, visited):
            if vertex in visited:
                return 0

            visited.add(vertex)

            for neighbor in graph[vertex]:
                height = 1 + calculate_height(neighbor, visited.copy())
                if vertex in height_dictionary:
                    height_dictionary[vertex] = max(height_dictionary[vertex], height)
                else:
                    height_dictionary[vertex] = height

            return height_dictionary[vertex]

        # start at leaf nodes
        for vertex, neighbors in graph.items():
            if len(neighbors) == 1:
                height_dictionary[vertex] = 1
            else:
                height_dictionary[vertex] = calculate_height(vertex, set())

        min_height_dictionary = {}
        min_height = math.inf
        for vertex, height in height_dictionary.items():
            min_height = min(height, min_height)
            if height in min_height_dictionary:
                min_height_dictionary[height].add(vertex)
            else:
                vertices = set()
                vertices.add(vertex)
                min_height_dictionary[height] = vertices

        return min_height_dictionary[min_height]


def main():
    sol = Solution()
    # 0 -> 3
    # 1 -> 3
    # 2 -> 3
    # 3 -> 0,1,2,4
    # 4 -> 3,5
    # 5 -> 4
    #print(sol.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])) # 3, 4

    #   2 - 0 - 1
    #       |
    #       3 - 4 - 5
    print(sol.findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]])) # 3

if __name__ == "__main__":
    main()