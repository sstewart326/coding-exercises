import heapq
from typing import List

class Word:
    def __init__(self, val, count):
        self.val = val
        self.count = count

    def __lt__(self, other):
        # first order by count
        if self.count != other.count:
            return self.count > other.count
        # then order by lexicographical order
        else:
            return self.val < other.val

# time - O(n + m log m + k log m)
# space - O(m + m + k)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        word_counts = {}
        # n
        for word in words:
            if word in word_counts:
                word_counts[word].count += 1
            else:
                word_counts[word] = Word(word, 1)
        # m == unique words
        for word in word_counts.values():
            heap.append(word)

        # m log m
        heapq.heapify(heap)
        answer = []
        # k
        for i in range(k):
            # log m
            answer.append(heapq.heappop(heap).val)
        return answer


def main():
    sol = Solution()
    print(sol.topKFrequent(["i","love","leetcode","i","love","coding"], 2))


if __name__ == "__main__":
    main()