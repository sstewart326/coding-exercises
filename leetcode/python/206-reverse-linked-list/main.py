from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # create a new var to track the reverse
    # that new var needs to start at None
    # for each iteration, point the curr node to the prev (prev is None at the beginning)
    # ensure prev is present for the next iteration

    # runtime - O(n) where n is the number of nodes
    # space - O(1) we are just tracking prev and head
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        # start of our new linked list
        prev = None

        while head:
            # track the next iteration before we update head.next for the reversal process
            next = head.next
            # set the next to the previous node to reverse paths
            head.next = prev

            # set prev to the current for the next iteration
            prev = head
            # set the curr to the next for the next iteration
            head = next

        return prev

def main():
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)

    one.next = two
    two.next = three
    three.next = four

    sol = Solution()
    head = sol.reverseList(one)
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    main()