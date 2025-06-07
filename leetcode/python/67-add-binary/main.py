# Input: a = "1010", b = "1011"
# Output: "10101"
#
#   need to track: right_pos, remainder
#   to calculate curr (top + bottom + remainder)
#       if that is 2, set curr to 0 and set remainder = 1
#       elseif 3, set curr to 1 and set remainder = 0
#       else set curr to sum and remainder = 0
#
#     1 0 1 0
#           ^
#     1 0 1 1
#           ^
# remainder = 0, sol = []
#  1 + 0 == 1, sol = [1], remainder = 0
#
#     1 0 1 0
#         ^
#     1 0 1 1
#         ^
# 1 + 1 + 0 == 2, sol = [0, 1], remainder = 1
#
#     1 0 1 0
#       ^
#     1 0 1 1
#       ^
# 0 + 0 + 1 == 1, sol = [1, 0, 1], remainder = 0
#
#     1 0 1 0
#     ^
#     1 0 1 1
#     ^
# 1 + 1 + 0 == 2, sol = [0, 1, 0, 1], remainder = 1
#
# if remainder > 0, add to sol
#  [1, 0, 1, 0, 1]
# time - O(n) where n is the largest of the two strings
# space - O(n+1) where n is the largest of the two strings. Worst case, we add a remainder at the front (thus +1)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        right_pos = 0
        remainder = 0
        solution = ""

        while right_pos < len(a) or right_pos < len(b):
            a_val = 0
            b_val = 0

            # get the top and bottom values
            # if the right_pos has overlapped our final value, set the value to 0
            if len(a) > right_pos:
                index = len(a)-1-right_pos
                a_val = int(a[index])
            if len(b) > right_pos:
                index = len(b)-1-right_pos
                b_val = int(b[index])

            sum = a_val + b_val + remainder

            # no special handling if we are not dealing with a remainder
            if sum < 2:
                solution = str(sum) + solution
                remainder = 0
            # else the sum is either 2 or 3. Thus, we can take the modulus 2 calculate the curr position
            else:
                solution = str(sum % 2) + solution
                remainder = 1

            right_pos += 1

        # if a remainder remains at the end, we need to prepend the solution with it
        if remainder == 1:
            return '1' + solution
        else:
            return solution


def main():
    sol = Solution()
    a = "1010"
    b = "1011"
    print(sol.addBinary(a, b)) # [1, 0, 1, 0, 1]

if __name__ == "__main__":
    main()