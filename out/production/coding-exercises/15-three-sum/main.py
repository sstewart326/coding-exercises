from typing import List


# time - O(n**2) - two pointer in nested. so outer loop runs through all numbers and the two pointer runs n-i number of times
# space - O(n) for the answer list
class Solution:

    def find_target(self, nums: List[int], target, left, right) -> List[List[int]]:
        answer = []
        left_start = left
        while left < right:
            # if we've already found all sums for this number, continue
            if left > left_start and nums[left] == nums[left - 1]:
                left += 1
                continue
            if nums[left] + nums[right] == target:
                answer.append([-target, nums[left], nums[right]])
                left += 1
                right -= 1
                continue

            # move left to increase sum
            # move right to decrease sum
            sum = nums[left] + nums[right]
            if sum < target:
                left += 1
            else:
                right -= 1

        return answer


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer: List[List[int]] = []
        sorted_nums = sorted(nums)

        # split this problem into 2
        # use i to create a target sum
        # then pass this target to another function to calculate 2sum
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1

            # when we have already determined all possible sums for this target, continue
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue

            # target sum is just the inverse of i
            target = -sorted_nums[i]

            answer = answer + self.find_target(sorted_nums, target, l, r)

        return list(answer)

class main():
   sol = Solution()
   print(sol.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
   print(sol.threeSum([1,-1,-1,0])) # [-1, 0, 1]
   print(sol.threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10])) #[[-10,5,5],[-5,0,5],[-4,2,2],[-3,-2,5],[-3,1,2],[-2,0,2]]

if __name__ == "__main__":
    main()