class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # for each char in magazine, add to dictionary with count
        # for each char in ransomNote, lookup from dictionary and subtract count
        #     if char doesn't exist or count is 0 before we subtract, return false

        chars = {}
        for c in magazine:
            if c in chars:
                count = chars.get(c)
                chars[c] = count + 1
            else:
                chars[c] = 1
        for c in ransomNote:
            if c not in chars:
                return False
            elif chars.get(c) == 0:
                return False
            else:
                count = chars.get(c) - 1
                chars[c] = count
        return True

def main():
    sol = Solution()
    print(sol.canConstruct("aa", "aab"))
    print(sol.canConstruct("aab", "aa"))


if __name__ == "__main__":
    main()