from typing import List


# time - O(n) size of nums
# space - O(n) size of nums
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        ans = [0] * len(nums)

        # at each iteration, max of (curr + val 2 positions back, val 1 position back)
        for index, num in enumerate(nums):
            if not ans:
                ans[0] = num
            elif index == 1:
                ans[1] = max(nums[1], nums[0])
            else:
                ans[index] = max(ans[index-1], nums[index]+ans[index-2])

        return ans[-1]



def main():
    sol = Solution()
    print(sol.rob([1,1,1,30,1,1,50])) # 81

if __name__ == "__main__":
    main()