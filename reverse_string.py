from typing import Reversible


def reverse_string(string):
    reversed_string = ''
    num = len(string) - 1

    for i in string:
        reversed_string += string[num]
        num -= 1

    return reversed_string

user_input = str(input("Please enter a word to be reversed: "))
print(user_input, sep='\n')
print(reverse_string(user_input))