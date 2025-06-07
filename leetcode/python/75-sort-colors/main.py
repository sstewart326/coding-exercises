from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        buckets = [0] * 3

        for num in nums:
            buckets[num] += 1

        for i in range(len(nums)):
            if buckets[0] > 0:
                buckets[0] -= 1
                nums[i] = 0
            elif buckets[1] > 0:
                buckets[1] -= 1
                nums[i] = 1
            else:
                nums[i] = 2



        """
        Do not return anything, modify nums in-place instead.
        """


def main():
    sol = Solution()
    nums = [2,0,2,1,1,0]
    sol.sortColors(nums)
    print(nums)


if __name__ == "__main__":
    main()