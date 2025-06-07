from typing import List


# calculate prefixes and postfixes
# [1, 2, 3, 4]     result ->     [24, 12, 8, 6]
#
# product -> (prefix)
# [1, 2, 6, 24]
# product <- (postfix)
# [24, 24, 12, 4]
#
# now calculate the result my taking product of prefix before i and suffix after i

# time - O(n) - iterate right to left to calculate the prefixes and left to right to calculate the suffixes
# space - O(n) - output array
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        size = len(nums)
        output = [1] * size

        if size <= 1:
            return nums

        # calculate prefix
        for i in range(size):
            prev = 1 if i == 0 else output[i - 1]
            output[i] = nums[i] * prev

        # calculate postfix (products from last element to first)
        # and then get the result (prev * next which excludes the curr element)

        for j in range(size-1, -1, -1):

            # calculating the suffix
            prev_suffix = 1 if j+1 == size else nums[j+1]
            nums[j] = nums[j] * prev_suffix

            # determining the output by multiplying prev suffix and next prefix
            next_prefix = 1 if j-1 < 0 else output[j-1]
            prev_suffix = 1 if j+1 == size else nums[j+1]
            output[j] = next_prefix * prev_suffix

        return output

def main():
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 3, 4]))
    print(sol.productExceptSelf([5]))

if __name__ == "__main__":
    main()