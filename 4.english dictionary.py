myDict = {
    'apple': ['a round fruit with red skin', '蘋果'],
    'banana': ['a long fruit with yellow skin', '香蕉'],
    'watermelon': ['a large, round fruit with green skin', '西瓜']
    }

def list_all_words():
    print('Your word list\n')
    for key, value in myDict.items():
        print('{} ({})\n{}'.format(key, value[1], value[0]))

def test_yourself():
    quit_the_test = False
    points = 0
    incorrect_word_list = []
    for key, value in myDict.items():
        while True:
            answer = input('\nWhich word matches the definition? Or [c]hinese, [p]ass, [q]uit\n{}'.format(value[0]))
            if answer == 'c':
                print('value[1]')
            elif answer == 'p':
                print('The correct answer is {}'.format(key))
                incorrect_word_list.append(key)
                break
            elif answer == 'q':
                quit_the_test = True
                break
            elif answer == key:
                points += 1
                print('Correct!')
                break
            else:
                print('It\'s not correct!')

        if quit_the_test == True:
            break

    print('\nScore {}/{}'.format(points, len(myDict)))
    print('Incorrect words list:')
    for key in incorrect_word_list:
        value = myDict[key]
        print('{} ({})\n{}'.format(key, value[1], value[0]))

def run():
    while True:
        cmd = input("""\nWelcome to your dictionary!
        1) Test yourself!
        2) List all words
        3) Exit\n""")
        if cmd == '1':
            test_yourself()
        elif cmd == '2':
            list_all_words()
        elif cmd == '3':
            break

run()
