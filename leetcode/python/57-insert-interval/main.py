from typing import List


# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#
# time - O(n) - traversing through the intervals. each interval is only of size 2 so we are not nesting loop thus not n*m
# space - O(n) - persisting those intervals into a new list
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if newInterval < interval[i], append newInterval + interval[i:]
        # if interval[i] < newInterval, append interval[i]
        # else we are overlapping so take mins and maxes
        # at the end, append newInterval to the result

        return_intervals = []

        for i in range(len(intervals)):
            # the new interval fits in before the tail, so we can return
            if newInterval[1] < intervals[i][0]:
                return_intervals.append(newInterval)
                return return_intervals + intervals[i:]
            # the new interval fits before the current index
            elif intervals[i][1] < newInterval[0]:
                return_intervals.append(intervals[i])
            # the new interval overlaps the current index
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

        return_intervals.append(newInterval)
        return return_intervals

def main():
    sol = Solution()
    print(sol.insert([[1,3],[6,9]], [2,5]))
    print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))

if __name__ == "__main__":
    main()