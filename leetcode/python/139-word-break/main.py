from typing import List

# create a dp array to track whether a certain index is the end of a segmented word
# this array will be one more than the len(s) to handle the base case where s is empty.
# in this case, the first index will be True. The last value in the array determines if
# s can be segmented
#
# "catsandog", ["cats","dog","an","cat"]
#                    c  a  t  s  a  n  d  o  g
#  can_segment = [T, F, F, T, T, F, T, F, F, T ]
#     True is the final index so return True
#
#   "catsandog", ["cats","dog","sand","and","cat"]
#                    c  a  t  s  a  n  d  o  g
#  can_segment = [T, F, F, T, T, F, F, T, T, F ]
#                                            ^
# F because dog can not be segmented because it is a part of another segmented word. Thus the T at index 7
#
# we need to track a max length of a dictionary word so we don't do any unnecessary traversing
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_size = 0
        for word in wordDict:
            if len(word) > max_size:
                max_size = len(word)

        word_set = set(wordDict)

        can_segment_word_at_index = [False] * (len(s) + 1)
        # base case where empty string is True
        can_segment_word_at_index[0] = True

        for i in range(1, len(s)+1):
            for j in range(i-1, max(i-max_size-1, -1), -1):
                segment = s[j:i]
                # can_segment_word_at_index[j] signifies the start of the last
                # segmented word. can_segment_word_at_index[j] is off by one when
                # compared to s[j] because we initiated can_segment_word_at_index = [True]
                if segment in word_set and can_segment_word_at_index[j]:
                    can_segment_word_at_index[i] = True
                    break

        return can_segment_word_at_index.pop()


def main():
    sol = Solution()
    print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
    print(sol.wordBreak("catsanddog", ["cats","dog","sand","and","cat"]))
    print(sol.wordBreak("ab", ["a","b"]))
    print(sol.wordBreak("cars", ["car","ca","rs"]))
    print(sol.wordBreak("a", ["a"]))


if __name__ == "__main__":
    main()