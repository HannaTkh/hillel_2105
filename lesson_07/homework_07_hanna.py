# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
separator = '- ' * 38
print(separator)
print('# task 1')


def multiplication_table(number):
    multiplier = 1
    while multiplier:
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1


multiplication_table(3)
print(separator)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

print('# task 2')


def sum_of_two_num(num1: int | float, num2: int | float) -> int | float:
    return num1 + num2


print('The sum of two numbers:', sum_of_two_num(10, 20))

print(separator)
# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print('# task 3')


def average(numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return 0


numbers1 = [10, 20, 30, 40]
average_value1 = average(numbers1)
print('Average', numbers1, '=', average_value1)

print(separator)
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print('# task 4')


def reverse_string_order(s):
    return "".join(reversed(list(s)))


print('String in reverse order:', reverse_string_order('1234 qwerty asdf'))

print(separator)
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print('# task 5')


def find_longest_word(some_text):
    words = some_text.split()
    if not words:
        return None
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print(f"The longest word is: {longest_word}")


text = "Your task is to write a function that takes a date in the form of three numbers"
find_longest_word(text)

print(separator)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

print('# task 6')


def find_substring(str01, str02):
    index = str01.find(str02)
    return index


string1 = "Hello, world!"
string2 = "world"

print(find_substring(string1, string2))

string1 = "The quick brown fox jumps over the lazy dog"
string2 = "cat"
print(find_substring(string1, string2))

print(separator)

# task 7
print('# task 7')


# Function for calculating the price of a product
def cost_of_computer(pay_for_month, number_of_months):
    return pay_for_month * number_of_months


print('If you pay 1179 UAH per month for 1,5 year,\n'
      f'The cost of smth will be', cost_of_computer(1179, 18), 'UAH')

print(separator)
# task 8
print('# task 8')


# Function for calculating the sum of two seas
def sum_areas_of_seas(area1: int | float, area2: int | float) -> int | float:
    return area1 + area2


print('Sum areas of two seas:', sum_areas_of_seas(436402, 37800), 'km2')

print(separator)
# task 9

print('# task 9')

adwentures_of_tom_sawer = """\
Tom   gave up the brush with reluctance in his .... face but alacrity
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


# Removing extra spaces between words
def removing_extra_spaces(some_string):
    without_extra_spaces = ' '.join(adwentures_of_tom_sawer.split())
    return without_extra_spaces


print(removing_extra_spaces(adwentures_of_tom_sawer))

print(separator)
# task 10

print('# task 10')


# Counting the number of letter "h" in a string
def quantity_of_h(string):
    number_of_h = adwentures_of_tom_sawer.count('h')
    return number_of_h


print('The letter "h" occurs in the text', quantity_of_h(adwentures_of_tom_sawer), 'times')

print(separator)
