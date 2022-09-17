# Author: Melissa Marie Perez
# Date: 9/17/2022
# Description:You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

from typing import Optional

from data_structures.ListNode import ListNode


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    l1_runner = l1
    l2_runner = l2

    sum_list = ListNode()
    sum_list_runner = sum_list
    carry = 0
    digit_sum = 0

    while l1_runner or l2_runner:
        if l1_runner and l2_runner:
            digit_sum = l1_runner.val + l2_runner.val + carry
        elif l2_runner is None:
            digit_sum = carry + l1_runner.val
        elif l1_runner is None:
            digit_sum = carry + l2_runner.val

        result = digit_sum % 10
        carry = 1 if digit_sum >= 10 else 0
        sum_list_runner.next = ListNode(val=result)
        sum_list_runner = sum_list_runner.next

        if l2_runner is not None:
            l2_runner = l2_runner.next
        if l1_runner is not None:
            l1_runner = l1_runner.next

    if carry:
        sum_list_runner.next = ListNode(val=carry)

    return sum_list.next
