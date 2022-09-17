# Author: Melissa Marie Perez
# Date: 9/17/2022
# Description: Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list. Return the linked list sorted as well.
from typing import Optional

from data_structures.ListNode import ListNode


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head
    front = ListNode(val=-102, next=head)
    prev, curr, runner = front, front.next, front.next.next

    while curr is not None and curr.next is not None:
        if curr.val != prev.val and curr.val != runner.val:
            curr = curr.next
            prev = prev.next
            runner = runner.next
        else:
            while runner is not None and curr.val == runner.val:
                runner = runner.next
            prev.next = runner
            curr = runner
            if curr is not None:
                runner = runner.next

    return front.next
