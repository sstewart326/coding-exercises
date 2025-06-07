
# runtime is O(n) - we need to visit each character in the string once
# runtime is O(n) - we are pushing characters into a stack
def is_valid(s):
    # push onto stack if not a closing bracket
    # pop from stack if closing bracket
        # if popped value is not opening char, return false
    # return true at end

    stack = []
    for c in s:
        if c != ')' and c != '}' and c != ']':
            stack.append(c)
        elif len(stack) > 0:
            popped = stack.pop()
            if c == ')' and popped != '(':
                return False
            elif c == ']' and popped != '[':
                return False
            if c == '}' and popped != '{':
                return False
        else:
            return False
    return len(stack) == 0

def main():
    print(is_valid("([)]"))
    print(is_valid("([])"))
    print(is_valid("[({"))
    print(is_valid("]"))


if __name__ == "__main__":
    main()