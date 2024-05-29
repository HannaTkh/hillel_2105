# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"'
                        '\n"That depends a good deal on where you want to get to," said the Cat.'
                        '\n"I don\'t much care where ——" said Alice.'
                        '\n"Then it doesn\'t matter which way you go," said the Cat.'
                        '\n"—— so long as I get somewhere," Alice added as an explanation.'
                        '\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')

print(alice_in_wonderland)


separator = '- '*38
print(separator)

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
together = (f'Area of the Black Sea = {436402} km2\n'
            f'Area of the Azov Sea = {37800} km2\n'
            f'Area of the Black Sea and the Sea of Azov together = {436402 + 37800} km2')

print(together)

print(separator)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

solution = (f'Total store products = {375291} products\n'
            f'First and second stocks = {250449} products\n'
            f'Second and third stocks = {222950} products\n'
            f'Task solution:\n'
            f'First stock = {375291 - 222950} products\n'
            f'Third stock = {375291 - 250449} products\n'
            f'Second stock = {375291 - (375291 - 250449) - (375291 - 222950)} products')
print(solution)

print(separator)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
computer_cost = (f'If you pay 1179 UAH per month for 1.5 years,\n'
                 f'the cost of the computer will be 1179 x 18 months = {1179 * 18} UAH')
print(computer_cost)

print(separator)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
remainder_from_division = (f'Remainder from division:\n'
                           f'a) 8019 % 8 = {8019 % 8}     d) 7248 % 6 = {7248 % 6}\n'
                           f'b) 9907 % 9 = {9907 % 9}     e) 7128 % 5 = {7128 % 5}\n'
                           f'c) 2789 % 5 = {2789 % 5}     f) 19224 % 9 = {19224 % 9}')
print(remainder_from_division)

print(separator)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
birthday_order = (f'Order for Iryna\'s birthday:\n'
                  f'Product name        Quantity        Price\n'
                  f'The big pizza       4               274 UAH\n'
                  f'The medium pizza    2               218 UAH\n'
                  f'Juice               4               35 UAH\n'
                  f'The Cake            1               350 UAH\n'
                  f'The water           3               21 UAH\n'
                  f'Total _____________________________ {274 + 218 + 35 + 350 +21} UAH')
print(birthday_order)

print(separator)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photoalbum = (f'To place all 232 photos in an album, 8 for one page,\n'
              f'Igor will need 232 / 8 = {232 // 8} pages')
print(photoalbum)

print(separator)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
journey = (f'Distance between Kharkov and Budapest = 1600 km\n'
           f'Gasoline consumption 9 liters per 100 km\n'
           f'Tank capacity 48 liters\n'
           f'1) For such a trip will be needed:\n'
           f'1600 / 100 * 9 = {1600 // 100 * 9} liters\n'
           f'2) During this trip, you will have to stop at a gas station:\n'
           f'144 / 48 = {144 // 48} times')
print(journey)

