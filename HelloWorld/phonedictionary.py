number_dictionary = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

phone = input('phone: ')
number_word = ''
for ch in phone:
    number_word += number_dictionary.get(ch, "!") + ' '
print(number_word)