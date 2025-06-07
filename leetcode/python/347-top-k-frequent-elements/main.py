import heapq
from heapq import heapify
from typing import List

# [1,1,1,2,2,3]
#            ^
class Solution:

    # n + m + m * log n
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        # n
        for num in nums:
            count, elem = counts.get(num, (0, num))
            count -= 1
            counts[num] = (count, elem)
            

        heap = []
        # m where m is the number of unique elements
        for count in counts.values():
            heap.append(count)

        ans = []

        # m
        heapify(heap)
        for i in range(k):
            # log n
            ans.append(heapq.heappop(heap)[1])

        return ans


def main():
    sol = Solution()
    print(sol.topKFrequent([1,1,2,2,1,3], 2))


if __name__ == "__main__":
    main()