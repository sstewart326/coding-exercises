from typing import List

# [1,3,4,2,2]
#  0 1 2 3 4
#      SF
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return -1

        slow = nums[0]
        fast = nums[0]

        # 1. detect cycle
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break

        # 2. find intersection
        fast = nums[0]
        while True:
            if fast == slow:
                return fast
            fast = nums[fast]
            slow = nums[slow]

def main():
    sol = Solution()
    print(sol.findDuplicate([1,3,4,2,2]))

if __name__ == "__main__":
    main()