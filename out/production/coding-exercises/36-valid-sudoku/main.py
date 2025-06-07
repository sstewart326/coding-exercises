from typing import List

# time - O(1) since we are only dealing with 9x9 grid
# space - O(1) since each dictionary  only persists up to 81 values
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # divide this into 9 grids
        starting_rows = [0, 3, 6]
        starting_columns = [0, 3, 6]

        row_vals = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
        column_vals = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}

        for row in starting_rows:
            for column in starting_columns:
                nums = set()
                for r in range(row, row + 3):
                    for c in range(column, column + 3):
                        curr = board[r][c]
                        if curr in nums or curr in row_vals[r] or curr in column_vals[c]:
                            return False
                        if board[r][c] == ".":
                            continue
                        nums.add(curr)
                        row_vals[r].add(curr)
                        column_vals[c].add(curr)

        return True

def main():
    sol = Solution()
    print(sol.isValidSudoku([["5","3",".",".","7",".",".",".","."]
                            ,["6",".",".","1","9","5",".",".","."]
                            ,[".","9","8",".",".",".",".","6","."]
                            ,["8",".",".",".","6",".",".",".","3"]
                            ,["4",".",".","8",".","3",".",".","1"]
                            ,["7",".",".",".","2",".",".",".","6"]
                            ,[".","6",".",".",".",".","2","8","."]
                            ,[".",".",".","4","1","9",".",".","5"]
                            ,[".",".",".",".","8",".",".","7","9"]]))

if __name__ == "__main__":
    main()