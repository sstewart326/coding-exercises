from typing import List


# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
# var to track curr_majority, count
#
# iterate nums
# if count = 0
#     set current_majority to num and increment count
# if curr_majority == curr
#     increment count
# if curr_majority != curr
#     decrement count
# time - O(n) where n is the number of nums
# space - O(1) we are only tracking count and curr_majority
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        curr_majority = None
        count = 0

        for num in nums:
            if count == 0:
                curr_majority = num
                count += 1
            elif curr_majority == num:
                count += 1
            else:
                count -= 1

        return curr_majority


def main():
    sol = Solution()
    print(sol.majorityElement([2,2,1,1,1,2,2]))


if __name__ == "__main__":
    main()