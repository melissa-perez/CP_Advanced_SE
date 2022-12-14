# Author: Melissa Marie Perez
# Date: 9/17/2022
# Description: Write a function that takes in two strings and returns true if
# the second string is substring of the first, and false otherwise.

def is_substring(word, sub):
    word_length = len(word)
    sub_length = len(sub)

    if sub_length < 1:
        return True

    for i in range(word_length):
        word_index = i
        sub_index = 0

        while sub_index < sub_length and word_index < word_length and word[word_index] == sub[sub_index]:
            sub_index += 1
            word_index += 1

        if sub_index == sub_length:
            return True

    return False


if __name__ == "__main__":
    print(is_substring("cat", "meow"))
