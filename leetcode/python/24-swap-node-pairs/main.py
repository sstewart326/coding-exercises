from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Left=1
# Right=2
# Right_Neighbor=3
#
# right.next = left
# left.next = right_neighbor
#
# [2,1,3,4]
#
# time - O(n)
# space - O(1)
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        ans = head.next
        prev = None
        while head and head.next:
            left = head
            right = head.next
            right_neighbor = right.next
            right.next = left
            left.next = right_neighbor
            if prev:
                prev.next = right

            prev = left
            head = right_neighbor

        return ans

def main():
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    ans = sol.swapPairs(head)
    while ans:
        print(ans.val)
        ans = ans.next

if __name__ == "__main__":
    main()