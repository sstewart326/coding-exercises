from typing import List


# target = sum / 2
#
# [1, 1, 2, 2]
#           ^
#  sum_set = {0, 2}
#
# [1, 1, 2, 2]
#        ^
#  sum_set = {0, 2, 4}
#
# [1, 1, 2, 2]
#     ^
#  sum_set = {0, 2, 4, 1, 3, 5}
#
# [1, 1, 2, 2]
#  ^
#  sum_set = {0, 2, 4, 1, 3, 5, 6}
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for num in nums:
            sum += num

        # we need an even number to evenly partition the list
        if sum % 2 != 0:
            return False

        target = sum / 2

        # 0 is the base case because for each iteration, we can either take the number or take 0
        sum_set = set()
        sum_set.add(0)

        buffer = set()

        for num in nums:
            for s in sum_set:
                curr = num + s
                if curr == target:
                    return True
                buffer.add(curr)
            sum_set = sum_set.union(buffer)
            buffer = set()
        return False

def main():
    sol = Solution()
    print(sol.canPartition([1,5,11,5]))
    print(sol.canPartition([2,2,1,1]))

if __name__ == "__main__":
    main()