from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#  1 -> 1 -> 2 <- 1 -> 1
#       S         F
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True

        slow = head
        fast = head.next
        mid_index = 0

        # get mid index using fast and slow pointer
        while fast:
            slow = slow.next
            mid_index += 1
            if fast.next:
                fast = fast.next.next
            else:
                fast = fast.next

        # reverse the second half of the list
        prev = None
        current = slow
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        # compare reversed list and head of list
        for i in range(mid_index):
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True

def main():
    sol = Solution()
    head = ListNode(1, next= ListNode(2, next= ListNode(3, next= ListNode(2, next = ListNode(1)))))
    print(sol.isPalindrome(head))

if __name__ == "__main__":
    main()