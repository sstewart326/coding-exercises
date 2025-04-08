from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

    # 5->7->10
    #        ^
    # 1->3->9
    #       ^

    if not list1:
        return list2
    if not list2:
        return list1

    head = None
    curr = None
    list1_next = list1
    list2_next = list2

    if list1.val <= list2.val:
        head = ListNode(list1.val)
        curr = head
        list1_next = list1.next
    else:
        head = ListNode(list2.val)
        curr = head
        list2_next = list2.next

    while list1_next is not None or list2_next is not None:
        if not list1_next:
            curr.next = list2_next
            list2_next = list2_next.next
        elif not list2_next:
            curr.next = list1_next
            list1_next = list1_next.next
        else:
            if list1_next.val <= list2_next.val:
                curr.next = list1_next
                list1_next = list1_next.next
            else:
                curr.next = list2_next
                list2_next = list2_next.next
        curr = curr.next
    return head


# 5->7->10
#        ^
# 1->3->9
#       ^
def main():
    five = ListNode(5)
    seven = ListNode(7)
    ten = ListNode(10)
    one = ListNode(1)
    three = ListNode(3)
    nine = ListNode(9)

    five.next = seven
    seven.next = ten

    one.next = three
    three.next = nine

    node = merge_two_lists(five, one)
    while node is not None:
        print(node.val)
        node = node.next

if __name__ == "__main__":
    main()