class Solution:

    # a palindrome is symmetric on both sides but can allow a unique character in the middle
    # so our algorithm needs to track even occurrences of characters but allow 1 odd character

    # runtime - o(c) where c is the number of characters
    # space - o(c) worst case, our str has all unique characters and our set fills up
    def longestPalindrome(self, s: str) -> int:
        # to keep track of chars with odd frequencies
        chars = set()
        # our return var
        length = 0

        for c in s:
            # if c count is even, add 2 to the length
            if c in chars:
                chars.discard(c)
                length += 2
            # else add the first occurence to the set
            else:
                chars.add(c)

        # if there is a char with an odd length, add 1 to the length
        if len(chars) > 0:
            return length + 1
        # else just return the length
        else:
            return length

def main():
    sol = Solution()
    print(sol.longestPalindrome("abccccdd")) # dccaccd 7


if __name__ == "__main__":
    main()