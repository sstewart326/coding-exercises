import heapq
from typing import List


class Solution:

    # The distance between two points on the X-Y plane is the Euclidean distance
    # (i.e., √(x1 - x2)2 + (y1 - y2)2).
    # x2 and y2 are the origin (0, 0) so we can remove those from the formula
    # square root isn't really relevant because we don't need to return the exact distance
    # rather we are just trying to identify which is closer. So we can remove that as well.
    # so our formula becomes x**2 + y**2
    def distance_between(self, x, y) -> int:
        return x**2 + y**2


    # time - O(n log k) we iterate through all points and log k for the operations on the heap (heappush, heappushpop)
    # space - O(k) heap that stores at most k items
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            x, y = point[0], point[1]
            if len(heap) < 2:
                # negate the value because heapq uses min heap (pops lowest)
                # we want the lowest number to become the highest number
                heapq.heappush(heap, (-self.distance_between(x, y), x, y))
            else:
                # pops smallest number
                heapq.heappushpop(heap, (-self.distance_between(x, y), x, y))

        return [(x, y) for _, x, y in heap]

def main():
    sol = Solution()
    print(sol.kClosest([[3,3],[5,-1],[-2,4]], 2)) # [[3,3],[-2,4]]

if __name__ == "__main__":
    main()