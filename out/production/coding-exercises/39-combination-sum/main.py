from typing import List



# time - O(2**target) In the worst case (when a candidate is 1), each position in your combination can either
# include or exclude that 1. So we continue to branch out
# space - O(target/min(candidates)) or just O(target) since the min candidate can recurse n num of times
class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        sorted_candidates = sorted(candidates)

        def recurse(index, sum, new_candidates):
            if sum == target:
                result.append(new_candidates.copy())
            else:
                while index < len(sorted_candidates) and sum + sorted_candidates[index] <= target:
                    new_candidate = sorted_candidates[index]
                    new_candidates.append(new_candidate)
                    recurse(index, new_candidate + sum, new_candidates)

                    # after we've reached the end, we need to pop the element
                    new_candidates.remove(new_candidate)
                    index += 1

        recurse(0, 0, [])
        return result

# [2,3,6,7] target = 7
# [2,2,3] [7]
def main():
    sol = Solution()
    print(sol.combinationSum([2,3,6,7], 7))
    print(sol.combinationSum([2,3,5], 8))
    print(sol.combinationSum([2], 1))

if __name__ == "__main__":
    main()