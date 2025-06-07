from typing import List

# time - O(n)
# space - O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, i = stack.pop()
                ans[i] = index - i

            stack.append((temp, index))

        return ans


def main():
    sol = Solution()
    print(sol.dailyTemperatures([73,74,75,71,69,72,76,73])) # [1,1,4,2,1,1,0,0]

if __name__ == "__main__":
    main()