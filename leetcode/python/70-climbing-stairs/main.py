# two ways to climb: 2 at a time or 1
# if n == 1
#    1                    1
# if n == 2
#    1    1      OR
#    2                    2
# if n == 3
#    1   1   1   OR
#    1   2       OR
#    2   1                3
# if n == 4
#    2   2          OR
#    1   1   1   1  OR
#    1   1   2      OR
#    2   1   1      OR
#    1   2   1             5
# if n == 5
#    2   2   1          OR
#    1   2   2          OR
#    2   1   2          OR
#    1   1   1   1   1  OR     8
#    2   1   1   1      OR
#    1   2   1   1      OR
#    1   1   2   1      OR
#    1   1   1   2
# This is a fib problem
class Solution:

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            # 1 only has 1 way to climb
            # 2 has 2 ways to climb
            return n

        # sets an array with all indexes to 0
        totals = [0] * n
        totals[0] = 1
        totals[1] = 2

        # start at 3 since we already have returns for the first 2
        for i in range(3, n + 1):
            prev = i - 1
            prev_prev = i - 2
            totals[i] = totals[prev] + totals[prev_prev]

        return totals[n]

def main():
    sol = Solution()
    print(sol.climbStairs(38))


if __name__ == "__main__":
    main()