
# time - O(n**2) because for each character, we are traversing surrounding characters
# space - O(n) where n could be the size of s
class Solution:
    def longestPalindrome(self, s: str) -> str:
        high = ""

        def check_palindrome(left, right):
            palindrome = ""
            while left >=0 and right < len(s) and s[left] == s[right]:
                if left == right:
                    palindrome = s[left]
                elif s[left] == s[right]:
                    palindrome = s[left] + palindrome + s[right]
                else:
                    break

                left -= 1
                right += 1
            return palindrome

        for i in range(len(s)):

            # even length
            even_high = check_palindrome(i, i+1)
            if len(even_high) > len(high):
                high = even_high

            # odd length
            odd_high = check_palindrome(i, i)
            if len(odd_high) > len(high):
                high = odd_high

        return high




def main():
    sol = Solution()
    print(sol.longestPalindrome("babadadadd"))
    print(sol.longestPalindrome("aooe"))
    print(sol.longestPalindrome("ccc"))


if __name__ == "__main__":
    main()