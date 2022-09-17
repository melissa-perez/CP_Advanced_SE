# Author: Melissa Marie Perez
# Date: 9/17/2022
# Description: A singly Linked List class
# implementation.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"<SLL -- val: {self.val}, next: {self.next}>"


if __name__ == '__main__':
    sll_test = ListNode(1, ListNode(2, ListNode(3)))
    print(sll_test)
