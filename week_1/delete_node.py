# Author: Melissa Marie Perez
# Date: 9/17/2022
# Description: You are given the node to be deleted node.
# You will not be given access to the first node of head.
from typing import Optional

from data_structures.ListNode import ListNode


def deleteNode(node: Optional[ListNode]):
    # modify in place basically
    node.val = node.next.val
    node.next = node.next.next
