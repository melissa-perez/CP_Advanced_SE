# Author: Melissa Marie Perez
# Date: 9/17/2022
# Description: Write a function that takes in two strings and returns true if
# the second string is substring of the first, and false otherwise.

def next_prime(prime):
    next = prime + 1

    while not is_prime(next):
        next += 1

    return next


def is_prime(prime):
    for i in range(2, prime - 1):
        if prime % i == 0:
            return False

    return True


if __name__ == "__main__":
    print(next_prime(19))
