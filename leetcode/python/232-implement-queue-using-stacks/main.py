# since we need to reverse the stack, any time we need to pop or peek,
# we should transfer all values from the push_stack to the peek_stack
class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []


    def push(self, x: int) -> None:
        if len(self.pop_stack) > 0:
            self.transfer()
        return self.push_stack.append(x)


    def pop(self) -> int:
        if len(self.push_stack) > 0:
            self.transfer()
        if len(self.pop_stack) > 0:
            return self.pop_stack.pop()
        else:
            return -1

    def peek(self) -> int:
        if len(self.push_stack) > 0:
            self.transfer()
        if len(self.pop_stack) > 0:
            return self.pop_stack[-1]
        else:
            return -1

    def empty(self) -> bool:
        return len(self.push_stack) == 0 and len(self.pop_stack) == 0

    def transfer(self):
        push_length = len(self.push_stack)
        pop_length = len(self.pop_stack)
        if push_length > 0:
            while len(self.push_stack) > 0:
                self.pop_stack.append(self.push_stack.pop())
        if pop_length > 0:
            while len(self.pop_stack) > 0:
                self.push_stack.append(self.pop_stack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

def main():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    while queue.peek() != -1:
        print(queue.pop())

    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek())
    print(queue.pop())



if __name__ == "__main__":
    main()