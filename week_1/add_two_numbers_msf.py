# Author: Melissa Marie Perez
# Date: 9/17/2022
# Description: You are given two non-empty linked lists representing two non-negative integers.
# The most significant digit comes first and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
from typing import Optional

from data_structures.ListNode import ListNode


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    l1_stack = []
    l2_stack = []
    result_stack = []
    createLLStacks(l1, l1_stack)
    createLLStacks(l2, l2_stack)
    carry_over = 0
    sum_nodes = 0
    while l1_stack or l2_stack:
        if l1_stack and l2_stack:
            num1 = l1_stack.pop(-1)
            num2 = l2_stack.pop(-1)
            sum_nodes = num1 + num2 + carry_over
        elif l1_stack:
            num1 = l1_stack.pop(-1)
            sum_nodes = num1 + carry_over
        elif l2_stack:
            num2 = l2_stack.pop(-1)
            sum_nodes = num2 + carry_over

        if sum_nodes >= 10:
            carry_over = 1
            sum_nodes %= 10
        else:
            carry_over = 0
        result_stack.append(sum_nodes)

    if carry_over:
        result_stack.append(carry_over)

    return createLL(result_stack)


def createLLStacks(ll, stack):
    while ll:
        stack.append(ll.val)
        ll = ll.next


def createLL(results):
    head = None
    sent = None

    while results:
        if head is None:
            head = ListNode(val=results.pop(-1))
            sent = ListNode(next=head)
        else:
            head.next = ListNode(val=results.pop(-1))
            head = head.next
    return sent.next
