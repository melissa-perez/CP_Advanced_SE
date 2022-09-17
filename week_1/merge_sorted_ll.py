# Author: Melissa Marie Perez
# Date: 9/17/2022
# Description: Merge the two lists in a one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
from typing import Optional

from data_structures.ListNode import ListNode


def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    l1_runner = l1
    l2_runner = l2
    sort_list = ListNode()
    sort_list_runner = sort_list

    while l1_runner is not None or l2_runner is not None:
        if l1_runner is None or l2_runner is not None and l1_runner.val > l2_runner.val:
            sort_list_runner.next = l2_runner
            l2_runner = l2_runner.next
        elif l2_runner is None or l1_runner is not None and l1_runner.val <= l2_runner.val:
            sort_list_runner.next = l1_runner
            l1_runner = l1_runner.next
        sort_list_runner = sort_list_runner.next

    return sort_list.next
