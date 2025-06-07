from typing import List

# [1,1,1,1,1,1,1,1,4], 5
#  L       R
class Solution:

    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)
        # If x is greater than total sum, impossible
        if x > total_sum:
            return -1
        # If x equals total sum, we need to remove all elements
        if x == total_sum:
            return len(nums)

        # flip the problem. instead of finding min operations required to trim ends,
        # let's find the max operations to sum(nums) - x
        target = total_sum - x
        curr_sum = 0
        left = 0
        max_operations = 0
        for right in range(len(nums)):
            curr_sum += nums[right]

            # Shrink window from left if sum exceeds target
            while curr_sum > target and left <= right:
                curr_sum -= nums[left]
                left += 1

            # If we found a valid subarray with sum = target
            if curr_sum == target:
                max_operations = max(max_operations, right - left + 1)

        if max_operations == 0:
            return -1
        else:
            return len(nums) - max_operations

def main():
    sol = Solution()
    print(sol.minOperations([5,2,3,1,1], 5))

if __name__ == "__main__":
    main()