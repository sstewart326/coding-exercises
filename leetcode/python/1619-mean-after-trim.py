from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        length = len(arr)
        elements_to_trim = int(length * .05)
        trimmed = arr[elements_to_trim:length-elements_to_trim]
        new_length = len(trimmed)
        return sum(trimmed) / new_length




def main():
    sol = Solution()
    print(sol.trimMean([6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]))

if __name__ == "__main__":
    main()