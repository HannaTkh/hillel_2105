# my_review_1 = 'Blab-bla\nsome info\\t some_info_2'
# my_review_2 = 'I don\'t want to do smth'
# my_review_3 = r'''Blab-bla
# some info\t some_info_2'''  # r = raw, сира строка
#
# print(my_review_1)
# print(my_review_3)
#
#
# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
# # task 01
# print(alice_in_wonderland)
#
# print(str(20/3)[:5])
# my_value = f'{10 + 5}, 11, {str(round(20/3, 4))}'
# print(type(my_value), my_value)
#
# my_name = 'Denis'
# my_full_name = f'{my_name} Merezhkin.\nMy age is 30 + 2 = {30 + 2}'  # f-strings
# print(my_full_name)
#
#
# black_sea_area = 436402
# azov_sea_area = 37800
#
#
#
# print('Area of the Black Sea =', black_sea_area, 'km2')
# print('Area of the Azov Sea =', azov_sea_area, 'km2' )
# print('Area of the Black Sea and the Sea of Azov together =', black_sea_area + azov_sea_area, 'km2' )
#
#
# together = (f'Area of the Black Sea = {black_sea_area} km2'
#             f'\nArea of the Azov Sea = {azov_sea_area} km2'
#             f'\nArea of the Black Sea and the Sea of Azov together = {black_sea_area + azov_sea_area} km2')
#
# print(together)
#
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

# all_stocks = 375291
# first_and_second = 250449
# second_and_third = 222950
# solution = (f'Total store products = {all_stocks} products\n'
#             f'First and second stocks = {first_and_second} products\n'
#             f'Second and third stocks = {second_and_third} products\n'
#             f'Task solution:\n'
#             f'First stock = {all_stocks - second_and_third} products\n'
#             f'Third stock = {all_stocks - first_and_second} products\n'
#             f'Second stock = {all_stocks - (all_stocks - first_and_second) - (all_stocks - second_and_third)} products')
# print(solution)

#

# # task 07
# """
# Знайди остачу від діленя чисел:
# a) 8019 : 8     d) 7248 : 6
# b) 9907 : 9     e) 7128 : 5
# c) 2789 : 5     f) 19224 : 9
# """
# remainder_from_division = (f'a) 8019 % 8 = {8019 % 8}     d) 7248 % 6 = {7248 % 6}\n'
#                            f'b) 9907 % 9 = {9907 % 9}     e) 7128 % 5 = {7128 % 5}\n'
#                            f'c) 2789 % 5 = {2789 % 5}     f) 19224 % 9 = {19224 % 9}')
# print(remainder_from_division)


# # task 08
# """
# Іринка, готуючись до свого дня народження, склала список того,
# що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
# для даного її замовлення.
# Назва товару    Кількість   Ціна
# Піца велика     4           274 грн
# Піца середня    2           218 грн
# Сік             4           35 грн
# Торт            1           350 грн
# Вода            3           21 грн
# """
# birthday_order = (f'Order for Iryna\'s birthday:\n'
#                   f'Product name        Quantity        Price\n'
#                   f'The big pizza       4               274 UAH\n'
#                   f'The medium pizza    2               218 UAH\n'
#                   f'Juice               4               35 UAH\n'
#                   f'The Cake            1               350 UAH\n'
#                   f'The water           3               21 UAH\n'
#                   f'Total _____________________________ {274 + 218 + 35 + 350 +21} UAH')
# print(birthday_order)

# # task 09
# """
# Ігор займається фотографією. Він вирішив зібрати всі свої 232
# фотографії та вклеїти в альбом. На одній сторінці може бути
# розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
# Ігорю, щоб вклеїти всі фото?
# """
# photoalbum = (f'To place all 232 photos in an album, 8 for one page, Igor will need 232 / 8 = {232 // 8} pages')
# print(photoalbum)

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