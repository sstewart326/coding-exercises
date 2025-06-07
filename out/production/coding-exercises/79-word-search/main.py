from typing import List


# time - O(m*n**4*L) where L is the length of the word. 4*L because we explore 4 directions up to the length of the word
# space - O(L) we recurse over the word
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def found(row, column, visited, remaining):
            if len(remaining) == 0:
                return True

            if row < 0 or row == len(board) or column < 0 or column == len(board[0]) or (row, column) in visited or board[row][column] != remaining[0]:
                return False

            visited.add((row, column))
            did_find = found(row + 1, column, visited, remaining[1:]) or found(row - 1, column, visited, remaining[1:]) or found(row, column + 1, visited, remaining[1:]) or found(row, column - 1, visited, remaining[1:])

            # remove coordinates from the already checked path
            visited.remove((row, column))
            return did_find

        for row in range(len(board)):
            for column in range(len(board[0])):
                if found(row, column, set(), word):
                    return True
        return False

def main():
    sol = Solution()
    print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
    print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
    # [["A","B","C","E"]
    # ["S","F","E","S"]
    # ["A","D","E","E"]]
    print(sol.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))



if __name__ == "__main__":
    main()