from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head

        odd_head = head
        odd_tail = head

        even_head = head.next
        curr_even = even_head
        # 1 -> 2 -> 3 -> 4 -> 5 -> None
        # O    E
        # 1 -> 3 -> 2 -> 4 -> 5 -> None
        #      O    E
        # 1 -> 3 -> 5 -> 2 -> 4 -> None

        while curr_even and curr_even.next:
            odd_tail.next = curr_even.next
            curr_even.next = odd_tail.next.next
            odd_tail = odd_tail.next
            odd_tail.next = even_head
            curr_even = curr_even.next
        return odd_head

def print_it(ll):
    print("\n\n\n NEW SOLUTION")
    while ll:
        print(ll.val)
        ll = ll.next

def main():
    sol = Solution()
    ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    sol.oddEvenList(ll)
    print_it(ll)
    ll = ListNode(1, ListNode(2))
    sol.oddEvenList(ll)
    print_it(ll)
    ll = ListNode(1)
    sol.oddEvenList(ll)
    print_it(ll)
    ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    sol.oddEvenList(ll)
    print_it(ll)



if __name__ == '__main__':
    main()