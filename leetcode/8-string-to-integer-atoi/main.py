# runtime - O(n) where n is the number of characters in the string
# space - O(n) - worst case is return_val holds the same characters as s
class Solution:

    # Whitespace: Ignore any leading whitespace (" ").
    # Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
    # Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
    # Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
    def myAtoi(self, s: str) -> int:
        index = 0
        sign = ""
        return_val = ""


        # -1 because 0 takes up one of the signed values
        MAX_INT = (2**31) - 1
        MIN_INT = -2**31

        while index < len(s) and s[index] == " ":
            index += 1

        if sign == "" and index < len(s) and s[index] == "-":
            sign = "-"
            index += 1
        if sign == "" and index < len(s) and s[index] == "+":
            index += 1

        while index < len(s) and s[index] == "0":
            index += 1

        while index < len(s) and s[index].isdigit():
            return_val += s[index]
            index += 1

        if return_val == "":
            return 0
        elif sign == "-":
            i = -int(return_val)
            if i < MIN_INT:
                return MIN_INT
            else:
                return i
        else:
            i = int(return_val)
            if i > MAX_INT:
                return MAX_INT
            else:
                return i

def main():
    sol = Solution()
    print(sol.myAtoi("-042"))
    print(sol.myAtoi("42"))
    print(sol.myAtoi("1337c0d3"))
    print(sol.myAtoi("0-1"))
    print(sol.myAtoi("words and 98"))
    print(sol.myAtoi("-91283472332"))



if __name__ == "__main__":
    main()