from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        result = None
        head = None
        while l1 or l2:
            if l1 is not None and l2 is not None:
                sum = l1.val + l2.val + remainder
                remainder = sum // 10
                num = sum if sum<10 else sum%10
                new_node = ListNode(num)
                if result:
                    result.next = new_node
                    result = result.next
                else:
                    result = new_node
                    head = result
                l1 = l1.next
                l2 = l2.next
            elif l1 is not None:
                sum = l1.val + remainder
                remainder = sum // 10
                num = sum if sum<10 else sum%10
                new_node = ListNode(num)
                if result:
                    result.next = new_node
                    result = result.next
                else:
                    result = new_node
                l1 = l1.next
            elif l2 is not None:
                sum = l2.val + remainder
                remainder = sum // 10
                num = sum if sum<10 else sum%10
                new_node = ListNode(num)
                if result:
                    result.next = new_node
                    result = result.next
                else:
                    result = new_node
                l2 = l2.next

        if remainder != 0:
            result.next = ListNode(remainder)

        return head

def main():
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    while result:
        print(result.val)
        result = result.next

if __name__ == "__main__":
    main()