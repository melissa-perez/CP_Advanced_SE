# Author: Melissa Marie Perez
# Date: 9/17/2022
# Description: Given a string s, return true if it is a palindrome, or false otherwise.


def isPalindrome(self, s: str) -> bool:
    s_length = len(s)
    left = 0
    right = s_length - 1
    s_copy = s.lower()

    while left < right:
        if not s_copy[left].isalnum():
            left += 1
            continue
        elif not s_copy[right].isalnum():
            right -= 1
            continue
        elif s_copy[left] != s_copy[right]:
            return False

        left += 1
        right -= 1
    return True
