# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version >= 4

class Solution:

    # for each iteration, check (high + low) / 2
    # once low >= high, return -1
    # 1 2 3 4 5     4 is first bad index
    # ^       ^    1 + (5 - 1) / 2 = 3
    # 1 2 3 4 5    3 is not bad, increment 3 by one and set this to low
    #     ^   ^
    # 1 2 3 4 5
    #       ^ ^    4 is bad. it is also low so we know there is no bad lower and we can return
    def traverse(self, low, high):
        # we can prevent stacked calls by returning early here
        # this is the lowest value we've seen so far so if it is bad, we can return
        if isBadVersion(low):
            return low

        # given we know there is at least one bad version, once low >= high, we can return low
        if low >= high:
            return low

        # prevents int overflows. better this than high + low // 2
        index_to_check = low + (high - low) // 2
        if isBadVersion(index_to_check):
            # continue to search left half
            return self.traverse(low, index_to_check)
        else:
            #,continue to search right half but start at index_to_check + 1
            # since we know index_to_check is not bad
            return self.traverse(index_to_check + 1, high)

    def firstBadVersion(self, n: int) -> int:
        return self.traverse(1, n)

def main():
    sol = Solution()
    size = 5
    print(sol.firstBadVersion(size))

if __name__ == "__main__":
    main()