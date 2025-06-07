from typing import List


class Solution:


    # [[1,10],[2,3],[4,5],[6,7],[8,9]]
    #           ^
    #
    #  start = 1        [[1,6], [8, 11] [15, 18]]
    #  end = 10
    #
    # if [i[0]] <= end, ignore start, set end to [i[1]]
    # else append [start, end]
    #
    # when last index = len(intervals - 1) end is max(end, i[1])

    # time - O(n) where n is the size of the intervals
    # space - O(n) we're tracking both the sorted_intervals and result array
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        sorted_intervals = sorted(intervals)
        result = []
        start = sorted_intervals[0][0]
        end = sorted_intervals[0][1]

        for i in range(1, len(sorted_intervals)):
            if i == len(sorted_intervals) - 1:
                if sorted_intervals[i][0] <= end:
                    result.append([start, max(end, sorted_intervals[i][1])])
                else:
                    result.append([sorted_intervals[i][0], sorted_intervals[i][1]])

            if sorted_intervals[i][0] <= end :
                end = max(end, sorted_intervals[i][1])
            else:
                result.append([start, end])
                start, end = sorted_intervals[i][0], sorted_intervals[i][1]

        return result

def main():
    sol = Solution()
    print(sol.merge([[1,3], [2,6] ,[8,10] ,[8,9], [9,11],[15,18], [2,4] ,[16,17]]))
    print(sol.merge([[1,10],[2,3],[4,5],[6,7],[8,9]]))

if __name__ == "__main__":
    main()