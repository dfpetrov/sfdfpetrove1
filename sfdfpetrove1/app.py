import random

WORDS = ('skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage',)

def get_random_word(word_list):
    return random.choice(word_list)

def get_word_display(word, try_letters=[]):
    result = ''
    for letter in word:
        if letter in try_letters:
            result += letter.upper() + ' '
        else:
            result += '_ '
        
    return result

def check_answer(word1, word2):
    return word1.lower().replace(' ', '') == word2.lower().replace(' ', '')

if __name__ == "__main__":
    
    secret_word = get_random_word(WORDS)
    secret_word_display = get_word_display(secret_word)
    
    penalties = 0
    try_count = 4

    print(f'Загаданное слово: {secret_word_display}')

    letters = []
    finish = False
    while penalties < try_count and not finish:
        
        secret_word_display = get_word_display(secret_word, letters)

        print('Введите букву:')
        letter = input()
        
        if letter in secret_word:
            letters.append(letter)
            secret_word_display = get_word_display(secret_word, letters)
            print(f'Есть такая: {secret_word_display}')
            finish = check_answer(secret_word, secret_word_display)
        else:
            penalties += 1
            print(f'Такой нет. Осталось попыток: {str(try_count-penalties)}')
            print(f'Загаданное слово: {secret_word_display}')
            if try_count-penalties == 0:
                print('Игра закончена')

    if penalties < try_count:
        print('Вы выиграли!!!')
    else:
        print(f'Вы проиграли:(. Было загадано слово: {secret_word}')
            
    