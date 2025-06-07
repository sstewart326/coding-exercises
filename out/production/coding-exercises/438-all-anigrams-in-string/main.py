from typing import List

# time - O(n) where n is the size of s
# space - O(k) where k is the size of the alphabet since each dictionary stores alpha keys
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []

        # dictionary to compare anagram target
        anagram_chars = {}
        for c in p:
            anagram_chars[c] = anagram_chars.get(c, 0) + 1

        indexes = []

        # the window that we will compare to our anagram_chars
        window_chars = {}

        # initial window
        for i in range(0, len(p)):
            window_chars[s[i]] = window_chars.get(s[i], 0) + 1

        left = 0
        right = len(p) - 1

        while right < len(s):
            if anagram_chars == window_chars:
                indexes.append(left)

            # remove from window if the char count is 1
            if window_chars[s[left]] == 1:
                window_chars.pop(s[left])
            # else, decrement the char count
            else:
                window_chars[s[left]] = window_chars[s[left]] - 1

            left += 1
            right += 1

            if right < len(s):
                # add the next position to the window
                window_chars[s[right]] = window_chars.get(s[right], 0) + 1

        return indexes

def main():
    sol = Solution()
    print(sol.findAnagrams("cbaebabacd", "abc"))

if __name__ == "__main__":
    main()