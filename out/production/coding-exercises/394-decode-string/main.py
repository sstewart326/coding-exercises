class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for c in s:
            if c == ']':
                sub_str = ''
                while stack[-1] != '[':
                    popped = stack.pop()
                    if popped == ']':
                        continue
                    sub_str = popped + sub_str
                # pop opening bracket
                stack.pop()

                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                # append back to the stack because we may need to concat later
                for _ in range(int(num)):
                    stack.append(sub_str)
            else:
                stack.append(c)

        return ''.join(stack)
                


def main():
    sol = Solution()
    print(sol.decodeString("3[a2[c]]"))

if __name__ == "__main__":
    main()