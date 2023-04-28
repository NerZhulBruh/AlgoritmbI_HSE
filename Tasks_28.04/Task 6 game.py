import random

def random_word():
    words = ['hard', 'exercise', 'for', 'me', 'its', 'impossible']
    return random.choice(words)

def hiding(word):
    return '-' * len(word)

def process_letter(letter, word, hidden_word):
    if letter in word:
        print("Эта буква есть в слове!")
        for i in range(len(word)):
            if word[i] == letter:
                hidden_word = hidden_word[:i] + letter + hidden_word[i+1:]
        print("Загаданное слово: ", hidden_word)
    else:
        print("Такой буквы нет в слове :(")
    return hidden_word

def game():
    word = random_word()
    hidden_word = hiding(word)
    print("Угадай слово: ", hidden_word)

    tries = 0
    max_tries = 9
    guessed = False
    
    while not guessed and tries < max_tries:
        letter = input("Введите букву: ")
        if len(letter) != 1:
            print("Пожалуйста, введите только одну букву!")
            continue
        if letter in hidden_word:
            print("Вы уже вводили эту букву!")
            continue
        hidden_word = process_letter(letter, word, hidden_word)
        if hidden_word == word:
            guessed = True
            print("А ты везучий, поздравляю!")
        else:
            print("Осталось попыток: ", max_tries - tries - 1)
            tries += 1

    if not guessed:
        print("Ты был очень близок к победе. Было загадано слово: ", word)

game()
