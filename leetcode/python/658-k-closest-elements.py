from typing import List


class Solution:

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k

        while left < right:

            mid_idx = left + ((right - left) // 2)

            # move left if left diff is < right diff
            if abs(x - arr[mid_idx]) <= abs(x - arr[mid_idx + k]):

                # mid is still a candidate so no +1
                right = mid_idx

            # else move right
            else:
                # mid is not a candidate so +1
                left = mid_idx + 1

        return arr[left:left+k]


def main():
    sol = Solution()
    print(sol.findClosestElements([1,1,2,3,4,5], 4, 3))

if __name__ == "__main__":
    main()