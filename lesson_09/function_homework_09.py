def average(numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return 0



def multiplication_table(number):
    multiplier = 1
    while multiplier:
        result = number * multiplier
        if result > 100:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1

# print(multiplication_table(200))

def sum_of_two_num(num1: int | float, num2: int | float) -> int | float:
    return num1 + num2



def reverse_string_order(s):
    return "".join(reversed(list(s)))




def find_longest_word(some_text):
    words = some_text.split()
    if not words:
        return None
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word




def quantity_of_h(string):
    number_of_h = string.count('h')
    return number_of_h