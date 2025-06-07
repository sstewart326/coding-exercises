from typing import List


# [1,2,3,4,5,6,7]   k=2
#
#  [7 6 1 2 3 4 5]
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)

        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1

        def swap(l, r):
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp

        while left <= right:
            swap(left, right)
            left += 1
            right -= 1

        # reverse front
        left = 0
        right = left + k - 1
        while left <= right:
            swap(left, right)
            left += 1
            right -= 1

        # reverse back
        left = 0 + k
        right = len(nums) - 1
        while left <= right:
            swap(left, right)
            left += 1
            right -= 1

def main():
    sol = Solution()
    arr = [1,2]
    sol.rotate(arr, 2)
    print(arr)

if __name__ == "__main__":
    main()