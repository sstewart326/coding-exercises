from typing import List



# time - n**2
# space - n
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        max_length = 1
        if len(nums) == 1:
            return max_length

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    count = max(dp[i], dp[j] + 1)
                    dp[i] = count
                    if count > max_length:
                        max_length = count
        return max_length


def main():
    sol = Solution()
    print(sol.lengthOfLIS([0,1,0,3,2,3]))

if __name__ == "__main__":
    main()