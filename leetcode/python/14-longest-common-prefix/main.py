from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        if len(strs) == 1:
            return strs[0]

        new_strs = strs[1:]
        for i in range(len(strs[0])):
            for str in new_strs:
                if len(str) == i or str[i] != strs[0][i]:
                    return ans
            ans += strs[0][i]

        return ans

def main():
    sol = Solution()
    print(sol.longestCommonPrefix(["flower","flow","flight"]))

if __name__ == "__main__":
    main()