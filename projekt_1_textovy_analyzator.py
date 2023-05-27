"""
projekt_1_textovy_analyzator.py: první projekt do Engeto Online Python Akademie
author: Anastassiya Manakova
email: anastassiyamanakova@gmail.com
discord: Anastassiya M.#8059
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

username = input('username: ')
password = input('password: ')
print(f'{"-"*50}')

if username in users and users[username] == password:
    print(f'Welcome to app, {username}\nWe have 3 texts to be analyzed.')
    print(f'{"-" * 50}')

    num_of_text = int(input('Enter a number btw. 1 and 3 to select: ')) -1
    print(f'{"-" * 50}')

    chosen_text = TEXTS[num_of_text]

    words = chosen_text.split()

    #how many words
    words_amount = len(words)
    print(f'There are {words_amount} words in the selected text.')

    #how many titlecase words
    words_tcased = 0
    for word in words:
        if word.istitle():
            words_tcased +=1
    print(f'There are {words_tcased} titlecase words.')

    #how many uppercase words
    words_ucased = 0
    for word in words:
        if word.isupper() and word.isalpha():
            words_ucased +=1
    print(f'There are {words_ucased} uppercase words.')

    #how many lowercase words
    words_lcased = 0
    for word in words:
        if word.islower():
            words_lcased +=1
    print(f'There are {words_lcased} lowercase words.')

    #how many numeric strings
    words_num = 0
    for word in words:
        if word.isnumeric():
            words_num +=1
    print(f'There are {words_num} numeric strings.')

    #sum of all numbers
    sum_of_num = 0
    for word in words:
        if word.isnumeric():
            sum_of_num += int(word)
    print(f'The sum of all numbers {sum_of_num}.')

    print(f'{"-" * 50}')

    #tab of occurences
    len_of_words_list = []
    for word in words:
        len_of_words_list.append(len(word))

    len_of_words_set = set(len_of_words_list)

    repeated_len = {}
    for i in len_of_words_list:
        repeated_len[i] = len_of_words_list.count(i)


    print(f'{"LEN|":<10} {"OCCURANCES":<20} {"|NR.":<10}')

    print(f'{"-" * 50}')

    for i in len_of_words_set:
        print(f'|{i:<10}|{"*"*repeated_len[i]:<20}|{repeated_len[i]:<10}')

else:
    print('uregistered user, terminating the program..')