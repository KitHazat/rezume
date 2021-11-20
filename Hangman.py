import random

word_list = ['промышленность']


def get_word():
    word = []
    word_all = random.choice(word_list).upper()
    for i in word_all:
        word.append(i)
    return word


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):
    word_consume = ['_' for _ in word]  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    while tries != 0:
        print('Давайте играть в угадайку')

        print(*word_consume, sep='')
        print('Введите Вашу букву:')
        letter = input().upper()
        if letter.isalpha():
            if letter not in guessed_letters:
                guessed_letters.append(letter)
            elif letter in guessed_letters:
                print('Эту букву вы уже вводили')
                continue
        else:
            print('Введите БУКВУ')
            continue

        if letter in word:
            for i in range(len(word)):
                if letter == word[i]:
                    word_consume[i] = letter
        elif letter not in word:
            print(display_hangman(tries))
            tries -= 1
        if word == word_consume:
            print(*word_consume, sep='*')
            print('Поздравляю, Вы выиграли!')
            break
        elif word != word_consume and tries == 0:
            print(display_hangman(tries))
            print(*word, sep='')


while True:
    start_game = input('Сыграем в игру? y/n')
    if start_game == 'y':
        while True:
            play(get_word())
            break
    else:
        break