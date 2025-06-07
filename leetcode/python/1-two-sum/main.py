

# time complexity - O(n) - at most we visit n nodes
# space complexity - O(n) - each value of nums get persisted into a dictionary
def find_indexes(nums, target):
    saved = {}

    for i, num in enumerate(nums):
        desired = target - num
        maybe = saved.get(desired)
        saved[num] = i
        if maybe is not None:
            return [maybe, i]

def main():
    print(find_indexes([1,4,2,6,4,7], 5))

if __name__ == "__main__":
    main()