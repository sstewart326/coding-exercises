from typing import List

# time - O(n) - iterating over nums
# space - O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_prod = -2**31

        curr_min = 1
        curr_max = 1
        for num in nums:
            if num == 0:
                curr_min = 1
                curr_max = 1

            temp_min = curr_min
            curr_min = min(num, num * curr_min, num * curr_max)
            curr_max = max(num, num * temp_min, num * curr_max)
            max_prod = max(curr_max, max_prod)

        return max_prod

def main():
    sol = Solution()
    print(sol.maxProduct([2,3,0,-1,5,-4,7,-8]))

if __name__ == "__main__":
    main()