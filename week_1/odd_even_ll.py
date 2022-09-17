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
