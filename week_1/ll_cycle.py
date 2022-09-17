# Author: Melissa Marie Perez
# Date: 9/17/2022
# Description: Given head, the head of a linked list,
# determine if the linked list has a cycle in it.
from typing import Optional

from data_structures.ListNode import ListNode


def hasCycle(head: Optional[ListNode]) -> bool:
    slow = head
    if not slow:
        return False
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True
