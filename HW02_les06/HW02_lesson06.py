# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

while True:
    input_word = input('Please input the word with "h": ')
    if 'h' in input_word.lower():
        break
    else:
        print('The word is without "h. Please try again: ')
