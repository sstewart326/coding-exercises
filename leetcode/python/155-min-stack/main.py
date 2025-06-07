class MinStack:

    def __init__(self):
        # (val, lowest)
        self.stack: [(int, int)] = []

    def push(self, val: int) -> None:
        curr_min = self.getMin()
        this_min = val if curr_min is None or val < curr_min else curr_min
        self.stack.append((val, this_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

def main():
    stack = MinStack()
    stack.push(4)
    stack.push(-2)
    stack.push(2)
    print(stack.getMin())
    print(stack.top())
    stack.pop()
    print(stack.getMin())
    stack.pop()
    print(stack.getMin())




if __name__ == "__main__":
    main()