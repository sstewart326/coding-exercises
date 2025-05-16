from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                nums[i - count] = nums[i]
        for i in range(len(nums)-count, len(nums)):
            nums[i] = 0

def main():
    sol = Solution()
    l = [0,1,0,3,12]
    sol.moveZeroes(l)
    print(l)

if __name__ == "__main__":
    main()