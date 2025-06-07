from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()
        for n in nums:
            if n in unique_nums:
                return True
            unique_nums.add(n)
        return False

def main():
    sol = Solution()
    print(sol.containsDuplicate([1,2,3,4,5,4]))

if __name__ == "__main__":
    main()