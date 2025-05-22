from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or head.next == None:
            return None

        behind = head
        ahead = head
        for i in range(n):
            ahead = ahead.next

        if not ahead:
            if n == 1:
                head.next = None
                return head
            else:
                return head.next

        while ahead.next:
            behind = behind.next
            ahead = ahead.next

        behind.next = behind.next.next

        return head

def main():
    sol = Solution()
    head = ListNode(1, ListNode(2))
    ans = sol.removeNthFromEnd(head, 2)
    while ans:
        print(ans.val)
        ans = ans.next

if __name__ == "__main__":
    main()