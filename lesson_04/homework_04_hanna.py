adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

separator = '- ' * 38
print(separator)

print("Task 01:")

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace('\n', ' ')
print(adwentures_of_tom_sawer)

print(separator)

# task 02 ==

print("Task 02:")

""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace('....', ' ')
print(adwentures_of_tom_sawer)

print(separator)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print("Task 03:")

adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer.split())
print(adwentures_of_tom_sawer)

print(separator)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("Task 04:")

print('The letter "h" occurs in the text' , adwentures_of_tom_sawer.count('h'), "times")

print(separator)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("Task 05:")

count = 0
for big_letter in adwentures_of_tom_sawer:
    if big_letter.isupper():
        count += 1
print('Number of capitalized words:', count)

print(separator)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("Task 06:")

second_appearance = adwentures_of_tom_sawer.find('Tom') + 1
print('The word Tom occurs a second time:', adwentures_of_tom_sawer.find('Tom', second_appearance), 'position')

print(separator)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
# adwentures_of_tom_sawer_sentences = None

print("Task 07:")

adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('. ')
print(adwentures_of_tom_sawer_sentences)

print(separator)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

print("Task 08:")

lower_04_sentence = adwentures_of_tom_sawer_sentences[3]
print(lower_04_sentence.lower())

print(separator)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("Task 09:")

for begin_sentence in adwentures_of_tom_sawer.split('.'):
    if begin_sentence.startswith(' By the time'):
        print('There is a sentence in the text that begins with "By the time"')

print(separator)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("Task 10:")

last_sentence = adwentures_of_tom_sawer_sentences[-1]
word_count = len(last_sentence.split())
print('The number of words in the last sentence:', word_count)

print(separator)


