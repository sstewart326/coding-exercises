from typing import List


# [3,2,1,0,4]
#. zero_index=3
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        zero_index = None

        for i in range(len(nums)-2,-1,-1):
            if not zero_index:
                if nums[i] == 0:
                    zero_index = i
            else:
                curr_jump = nums[i]
                if curr_jump + i > zero_index:
                    zero_index = None
        return zero_index is None

def main():
    sol = Solution()
    print(sol.canJump([0,1]))


if __name__ == "__main__":
    main()