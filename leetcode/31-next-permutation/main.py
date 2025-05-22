from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 1:
            return

        pivot_index = 0
        # 1. find first decreasing index (this signifies a number that is lower than the max)
        left, right = len(nums) - 2, len(nums) - 1
        while left >= 0:
        # 2. swap last index with smaller number's index
            for i in range(len(nums) - 1, left-1, -1):
                if nums[i] > nums[left]:
                    nums[i], nums[left] = nums[left], nums[i]
                    pivot_index = left + 1
                    right = len(nums) - 1
        # 3. reverse everything (since current order is highest num and we want lowest)
                    while pivot_index < right:
                        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
                        pivot_index, right = pivot_index + 1, right - 1
                    return
            left -= 1
            right -= 1

        # if we get here, the number is already max
        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

def main():
    sol = Solution()
    arr = [3,2,1]
    sol.nextPermutation(arr)
    print(arr)

if __name__ == "__main__":
    main()