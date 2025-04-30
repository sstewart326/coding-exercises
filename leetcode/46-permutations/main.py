from typing import List

# time - O(n!) - since it is a permutation
# space - O(n!) - the size of the return list
class Solution:
    # Input: nums = [1,2,3]
    # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    #
    # [1 2 3] [2 3] [3] [] - backtrack until empty array
    # now insert before and after each element
    # [3]
    # [2 3] [3 2]
    # [1 2 3] [2 1 3] [2 3 1] [1 3 2] [3 1 2] [3 2 1]
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0:
            return [[]]

        permutations = self.permute(nums[1:])

        new_permutations = []
        for permutation in permutations:
            # + 1 because we want to insert the nums[0] after the last num in the permutation as well
            for index_to_insert in range(len(permutation) + 1):
                copy = permutation.copy()
                # nums[0] because each recursive call cuts off the head
                copy.insert(index_to_insert, nums[0])
                new_permutations.append(copy)
        return new_permutations

def main():
    sol = Solution()
    print(sol.permute([1,2,3]))

if __name__ == "__main__":
    main()