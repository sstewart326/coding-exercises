

# time - O(s) or 2s where s is  the size of the str because the right pointer
#        traverses the entire string and the left pointer could also do the same
# space - O(min(s, n) where s is unique characters that get saved to curr and n is
#         the length of the string
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            chars.add(s[right])

            # plus 1 since we start at 0 index
            longest = max(longest, right - left + 1)

        return longest

def main():
    sol = Solution()
    print(sol.lengthOfLongestSubstring("pwhwkew")) # 3
    print(sol.lengthOfLongestSubstring("abcabcbb")) # 3
    print(sol.lengthOfLongestSubstring("bbbbb")) # 1
    print(sol.lengthOfLongestSubstring("dvdf")) # 3

if __name__ == "__main__":
    main()