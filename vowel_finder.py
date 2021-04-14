def vowel_finder(string):
    vowels = ['a','e','i','o','u']
    lower_string = string.lower()
    num_vowels = 0

    for char in lower_string:
        for vowel in vowels:
            if char == vowel:
                num_vowels += 1
    return 'The number of vowels is :' + str(num_vowels)

user_input = str(input("Please enter a word or sentence and I will count the # of vowels: "))

print(user_input)
print(vowel_finder(user_input))