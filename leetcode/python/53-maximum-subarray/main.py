from typing import List

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
#
#     3  -4   7 -5   3 -1 -6  9
#  [-2, 1, -3, 4, -1, 2, 1, -5, 4]
class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_num = nums[0]
        last_sum = nums[0]

        # [ 1, 2, 3, -1, 6]
        6

        for i in range(1, len(nums)):

            # this is where we sum
            # if the current value is greater than the sum, just take the current value
            last_sum = max(nums[i], last_sum + nums[i])

            # if curr is > max, set max
            max_num = max(max_num, last_sum)

        return max_num


def main():
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

if __name__ == "__main__":
    main()