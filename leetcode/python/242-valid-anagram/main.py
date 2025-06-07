# time complexity - O(n) - because worst case, we visit each character in both strings m + n
# space complexity - O(k) - k is the ASCII characters
class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        # Early length check
        if len(s) != len(t):
            return False

        # Create frequency dictionary in one pass
        char_count = {}
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1

        # Decrement counts in one pass
        for c in t:
            if c not in char_count or char_count[c] == 0:
                return False
            char_count[c] -= 1

        return True


def main():
    sol = Solution()
    print(sol.isAnagram("ant", "nat"))
    print(sol.isAnagram("ant", "nadt"))

if __name__ == "__main__":
    main()