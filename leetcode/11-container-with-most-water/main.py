from typing import List

# time - O(n) where n is the size of the height list
# space - O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max = 0

        # always move pointer from the smallest position
        # for each position calculate the area by taking the min(left, right) * (right - left)

        while left < right:
            left_val = height[left]
            right_val = height[right]
            curr = min(left_val, right_val) * (right - left)
            if curr > max:
                max = curr

            if left_val < right_val:
                left += 1
            else:
                right -= 1

        return max

def main():
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7])) # 49

if __name__ == "__main__":
    main()