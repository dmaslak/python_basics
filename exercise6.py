# Урок 2, упражнение 6

# Объявляем переменные
from typing import final


items_list = []
command = ''

# Запрашиваем данные у пользователя с помощью while
while command != 'завершить':
    item_dict = {}
    command = input('Что вы хотите сделать: "добавить товар" или "завершить" ')
    if command == 'добавить товар':
        item_id = input('Введите id товара ')
        item_name = input('Введите название товара ')
        item_price = input('Введите цену товара ')
        item_qty = input('Введите количество единиц товара на складе ')

        # Формируем словарь с характеристиками
        item_dict['name'] = item_name
        item_dict['price'] = item_price
        item_dict['quantity'] = item_qty


        # Формируем кортеж и присоединяем его к основному списку
        item_tuple = (item_id, item_dict)
        items_list.append(item_tuple)
    elif command == 'завершить':
        break
    else:
        command = input('Пожалуйста вводите только "добавить товар" или "завершить"')
        continue

        
# Выходим из цикла и формируем словарь с аналитикой
print('Мы вышли из цикла и подготовили словарь с аналитикой')

names_list = []
price_list = []
quantity_list = []
final_dict = {}

for item in items_list:
    names_list.append(item[1]['name'])
    price_list.append(item[1]['price'])
    quantity_list.append(item[1]['quantity'])

final_dict['names'] = names_list
final_dict['prices'] = price_list
final_dict['quantities'] = quantity_list

print(final_dict)