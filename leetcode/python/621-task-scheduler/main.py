import heapq
from typing import List
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counts = {}
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1

        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)

        time = 0
        cooldown = deque()
        while max_heap or cooldown:

            time += 1

            # Re-add tasks whose cooldown has expired
            if cooldown and cooldown[0][0] == time:
                _, cnt = cooldown.popleft()
                heapq.heappush(max_heap, cnt)

            if max_heap:
                cnt = heapq.heappop(max_heap)
                if cnt < -1:
                    cooldown.append((time + n + 1, cnt + 1))

        return time


def main():
    # Input: tasks = ["A","A","A","B","B","B"], n = 2
    #
    # Output: 8
    #
    # Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
    sol = Solution()

    print(sol.leastInterval(["A","A","A","B","B","B"], 2)) # 8
    print(sol.leastInterval(["A","C","A","B","D","B"], 1))
    print(sol.leastInterval(["B","C","D","A","A","A","A","G"], 1)) # 8


if __name__ == "__main__":
    main()