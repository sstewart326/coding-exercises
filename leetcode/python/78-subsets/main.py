from typing import List


# Input: nums = [1,2,3]
#
# time - O(n * 2**n) because we are iterating through each num but after each iteration, we
#                    double the number of iterations required for our inner loop
# space - O(n * 2**n)
class Solution:

    # subset array [ [] ]
    # iterate over nums and iterate over subset and add each num to the subset
    def subsets(self, nums: List[int]) -> List[List[int]]:

        output = [[]]

        buffer = []

        for num in nums:
            for subset in output:
                copy = subset.copy()
                copy.append(num)
                buffer.append(copy)

            output.extend(buffer)
            buffer = []

        return output



def main():
    # Input: nums = [1,2,3]
    # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    sol = Solution()
    for line in sol.subsets([1,2,3]):
        print(line)


if __name__ == "__main__":
    main()