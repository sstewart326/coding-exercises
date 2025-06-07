
# Input: n = 4, k = 2
# Output: 7

# Explanation: You can distribute 4 candies into 2 bags in 7 ways:
# (1), (2,3,4)
# (1,2), (3,4)
# (1,3), (2,4)
# (1,4), (2,3)
# (1,2,3), (4)
# (1,2,4), (3)
# (1,3,4), (2)
class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        # track prev [[0]]
        # remaining = [1->n]
        # range 0 to candy -1 because one bag needs at least one candy
        # range 0 to bag
        # copy prev and append candy[i], and delete from remaining

        unique_ways = set()
        prev = set()
        remaining = [i for i in range(1, n)]

        for candy in range(n-1):
            for bag in range(k):
                unique_ways

        pass

def main():
    sol = Solution()
    print(sol.waysToDistribute())

if __name__ == "__main__":
    main()