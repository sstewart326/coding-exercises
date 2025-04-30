class Solution:

    def memoized(self, m, n):
        memo = {}

        def traverse(row, column, count):

            if (row, column) in memo:
                return memo[(row, column)]

            # add one once we reach the bottom right corner
            if row == m - 1 and column == n - 1:
                return count + 1

            # just return current count without incrementing if we go out of bounds
            elif row == m or column == n:
                return count

            # we can take two paths, down or right
            memo[row, column] = traverse(row + 1, column, count) + traverse(row, column + 1, count)
            return memo[row, column]

        return traverse(0, 0, 0)

    # time - O (m * n) we need to traverse the entire matrix
    # space - O (m * n) for sum_matrix
    def dp(self, m, n):

        sum_matrix = [ [1 for _ in range(n) ] for _ in range(m)  ]

        # base case. From the last coordinates, there is only one path
        sum_matrix[m-1][n-1] = 1

        for row in range(len(sum_matrix)-1, -1, -1):
            for column in range(len(sum_matrix[0])-1, -1, -1):

                # skip base case
                if row == m-1 and column == n-1:
                    continue

                right_sum = 0
                if column + 1 < len(sum_matrix[0]):
                    right_sum = sum_matrix[row][column + 1]

                down_sum = 0
                if row + 1 < len(sum_matrix):
                    down_sum = sum_matrix[row + 1][column]

                sum_matrix[row][column] = right_sum + down_sum

        return sum_matrix[0][0]


    def uniquePaths(self, m: int, n: int) -> int:
        # return self.memoized(m, n)
        return self.dp(m, n)


def main():
    sol = Solution()
    print(sol.uniquePaths(23, 12))

if __name__ == "__main__":
    main()