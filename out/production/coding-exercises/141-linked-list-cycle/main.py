from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Fast/Slow Pointer Solution
# time - O(n) where n is the number of nodes in our list
# space - O(1) - we're only using two pointers (fast and slow)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False


def main():

    three = ListNode(3)
    two = ListNode(2)
    zero = ListNode(0)
    neg_four = ListNode(-4)
    three.next = two
    two.next = zero
    zero.next = neg_four
    neg_four.next = two
    sol = Solution()
    print(sol.hasCycle(three)) # true

    neg_four.next = None
    print(sol.hasCycle(three)) # false


if __name__ == "__main__":
    main()