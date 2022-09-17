# Author: Melissa Marie Perez
# Date: 9/17/2022
# Description: Given the head of a singly linked list, group all the nodes with odd indices together
# followed by the nodes with even indices, and return the reordered list.
from typing import Optional
from data_structures.ListNode import ListNode


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    # check for empty ll
    if not head:
        return head
    # create the sentinel node and pointers to partitions
    sentinel = ListNode(next=head)
    odd_runner = sentinel.next
    even_head = even_runner = odd_runner.next
    # loop and create lists
    while odd_runner.next and even_runner.next:
        temp = even_runner.next
        even_runner.next = temp.next
        odd_runner.next = temp
        odd_runner = odd_runner.next
        even_runner = even_runner.next
    # hook up the lists
    odd_runner.next = even_head
    return sentinel.next


if __name__ == '__main__':
    # empty list
    test_sll = ListNode()
    print(oddEvenList(test_sll))
    # singleton list
    test_sll = ListNode(1)
    print(oddEvenList(test_sll))
    # double list
    test_sll = ListNode(1)
    print(oddEvenList(test_sll))
    # test case 1
    test_sll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(oddEvenList(test_sll))
    # test case 2
    test_sll = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
    print(oddEvenList(test_sll))
