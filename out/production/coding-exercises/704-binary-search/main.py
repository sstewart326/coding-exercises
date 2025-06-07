from typing import List


# runtime - O(logn) - each iteration cuts the list in half
# space - O(1) - just keeping track of indexes
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # keep track of low index and high index
        # [-1,0,3,5,9,12]  target 9
        #   l          h   int((5 - 0) / 2) = 2 + low (0)
        # [-1,0,3,5,9,12]  target 9
        #       ^          3 < 9 so set low index to 2
        #                  int((5 - 2) / 2) = 1 + low (2)
        # [-1,0,3,5,9,12]  target 9
        #         ^        5 < 9 so set low index to 3
        #                  int((5-3) / 2) = 1 + low (3)
        # [-1,0,3,5,9,12]  target 9
        #           ^      9 == 9, return index

        low_idx = 0
        high_idx = len(nums) - 1

        while low_idx <= high_idx:
            target_idx = int((high_idx + low_idx) / 2)
            if nums[target_idx] == target:
                return target_idx
            elif nums[target_idx] > target:
                high_idx = target_idx - 1
            else:
                low_idx = target_idx + 1

        return -1







def main():
    sol = Solution()
    print(sol.search([-1,0,3,5,9,12], 9))
    print(sol.search([2,5], 5))
    print(sol.search([2,5], 2))
    print(sol.search([2,5], 8))

if __name__ == "__main__":
    main()