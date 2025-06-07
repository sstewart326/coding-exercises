from logging import addLevelName
from typing import List

# time - O(n * k log k) where n is the size of strs and k is the size of each str for the sort operation
# space - O(n * k) k is the avg size of each str and represents the keys in the dictionary
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for str in strs:
            sorted_str = "".join(sorted(str))
            original_values = anagram_dict.get(sorted_str, [])
            original_values.append(str)
            anagram_dict[sorted_str] = original_values

        return list(anagram_dict.values())

def main():
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(sol.groupAnagrams(["a"]))


if __name__ == "__main__":
    main()