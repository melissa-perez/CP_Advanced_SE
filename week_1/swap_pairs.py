# Author: Melissa Marie Perez
# Date: 9/17/2022
# Description: Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)


from data_structures.ListNode import ListNode


def swapPairs(head: ListNode) -> ListNode:
    if not head:
        return head

    front = ListNode(next=head)
    prev, curr, runner = front, front.next, front.next.next

    while curr is not None and runner is not None:
        # perform the switch
        curr.next = runner.next
        runner.next = curr
        prev.next = runner

        # updates the pointers
        prev = curr
        curr = curr.next

        if curr is not None:
            runner = curr.next

    return front.next
