from typing import List


# most competitive subsequence == subsequence with lexicographically smaller ints of k size

# [2,4,3,3,5,4,9,6]. k=4
#
#.   stack []
#.        pop and push when:
#.            curr < stack.peek && there is enough trailing elements to satisfy k
#                       k is satisfied if number of indexes left >= k - (num of elements in stack - 1)
#.        push when:
#             num of elements in stack is < k
#.
#     [2,3,3,4]
class Solution:

    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        nums_size = len(nums)

        for idx, num in enumerate(nums):

            indexes_remaining = nums_size - (idx + 1)

            while stack and num < stack[-1] and indexes_remaining >= k - len(stack):
                stack.pop()

            if len(stack) < k:
                stack.append(num)

        return stack

def main():
    sol = Solution()
    print(sol.mostCompetitive([71,18,52,29,55,73,24,42,66,8,80,2], 3))

if __name__ == "__main__":
    main()