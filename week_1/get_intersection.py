# Author: Melissa Marie Perez
# Date: 9/17/2022
# Description: Given the heads of two singly linked-lists headA and headB,
# return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

from typing import Optional, Union

from data_structures.ListNode import ListNode


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Union[ListNode, None]:
    d1 = headA
    d2 = headB
    while d1 != d2:
        if d1.next is None and d2.next is None:
            return None
        elif d1.next is None:
            d1 = headB
            d2 = d2.next
        elif d2.next is None:
            d2 = headA
            d1 = d1.next
        else:
            d1 = d1.next
            d2 = d2.next
    return d1
