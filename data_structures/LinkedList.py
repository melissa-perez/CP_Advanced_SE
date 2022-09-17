# Author: Melissa Marie Perez
# Date: 9/17/2022
# Description: A singly Linked List class
# implementation.

class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"<Test a:{self.a} b:{self.b}>"

if __name__ == '__main__':
    print("Hello, world!")
