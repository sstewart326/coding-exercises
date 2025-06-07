from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        # <= because nums could just be [5]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # left portion is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # right portion is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


# [6,7,8,9,0,1,2,3,4,5]
#  ^                 ^   tgt = 8
#
# if L < M, left is sorted
# if M > R, right is sorted

# if L < tgt > M, target is in left
# if R
def main():
    sol = Solution()
    print(sol.search([4,5,6,7,0,1,2], 0))
    print(sol.search([4,5,6,7,0,1,2], 3))
    print(sol.search([1], 0))
    print(sol.search([1,3], 2))

if __name__ == "__main__":
    main()