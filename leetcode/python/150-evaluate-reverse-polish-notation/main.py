from typing import List


# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#
# time - O(c) where c is the number of characters in the string
# space - O(c) worst case is O(n/2) where stack contains all nums followed by operators
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            # better to start with characters since negative ints are difficult to identify
            if token in ["+", "-", "*", "/"]:
                second_num = int(stack.pop())
                first_num = int(stack.pop())

                if token == '+':
                    stack.append(first_num + second_num)
                elif token == '-':
                    stack.append(first_num - second_num)
                elif token == '*':
                    stack.append(first_num * second_num)
                elif token == '/':
                    # Integer division toward zero
                    stack.append(int(first_num / second_num))
            else:
                stack.append(token)

        return stack.pop()

def main():
    sol = Solution()
    print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) # 22
    print(sol.evalRPN(["4","13","5","/","+"])) # 6

if __name__ == "__main__":
    main()