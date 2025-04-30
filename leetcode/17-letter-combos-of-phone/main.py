from typing import List


# time - O(4**n) 4 is the max length of the character array
# space - O(4**n) combinations + n recursive stack
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            "0": [],
            "1": [],
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }

        if len(digits) == 0:
            return []

        def combine(digits: str):
            if digits == "":
                return [""]

            combinations = combine(digits[1:])
            new_perms = []
            for perm in combinations:
                for char in keyboard[digits[0]]:
                    # append curr char first since we are working bottom up
                    new_perms.append(char + perm)
            return new_perms

        return combine(digits)

def main():
    sol = Solution()
    print(sol.letterCombinations("23"))

if __name__ == "__main__":
    main()