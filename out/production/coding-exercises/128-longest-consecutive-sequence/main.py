from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        num_set = set(nums)
        max = 1
        visited = set()

        for num in nums:
            if num in visited:
                continue
            else:
                visited.add(num)

            is_start = num - 1 not in num_set
            if is_start:
                count = 1
                while num + 1 in num_set:
                    visited.add(num + 1)
                    count += 1
                    num += 1
                if count > max:
                    max = count
        return max

def main():
    sol = Solution()
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(sol.longestConsecutive([100,4,200,1,3,2]))
    print(sol.longestConsecutive([1,0,1,2]))

if __name__ == "__main__":
    main()