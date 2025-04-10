from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#
# 1->2->3->4->None             1->2->3->4->5->None
# ^                            ^
# 1->2->3->4->None             1->2->3->4->5->None
#    L  R                         L  R
# 1->2->3->4->None             1->2->3->4->5->None
#       L      R                     L     R
# right is none, return L      right.next is none, return L

# time - O(n/2) / O(n) where n is the number of nodes
# space - O(1) just keeping track of the left and right
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        left = head
        right = head

        while right and right.next:
            left = left.next
            right = right.next.next

        return left


def main():
    sol = Solution()
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    one.next = two
    two.next = three
    three.next = four

    print(sol.middleNode(one).val)


if __name__ == "__main__":
    main()