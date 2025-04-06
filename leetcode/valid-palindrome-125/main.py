# time complexity - O(N) - at best we only traverse the strings to the mid-point
# space complexity - O(1) - re-using i, j
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # racecar
        # ^     ^

        if len(s) == 1:
            return True

        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True




def main():
    sol = Solution()
    print(sol.isPalindrome("car"))
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))
    print(sol.isPalindrome("0P"))

if __name__ == "__main__":
    main()