'''
Cкрипт на Python, который выполняет анализ данных по покупкам в магазине (список из словарей)
'''

#1. Общая выручка
def total_revenue(purchases):
    res = []
    for i in range(len(purchases)):
        res.append(purchases[i]['price'] * purchases[i]['quantity'])
    print(f'Общая выручка: {sum(res)}')

    
#2. Список товаров по категориям
def items_by_category(purchases):
    res = {}
    for i in range(len(purchases)):
        res.setdefault(purchases[i]['category'], []).append(purchases[i]['item'])
    print(f'Товары по категориям: {res}')

#3. Список покупок, где цена превышает заданное значение
def expensive_purchases(purchases, min_price):
    res = []
    for i in range(len(purchases)):
        if purchases[i]['price'] >= min_price:
            res.append(purchases[i])
    print(f'Покупки дороже {min_price}: {res}')


#Средняя цена товара по категориям
def average_price_by_category(purchases):
    res = {}
    avg = {}
    for i in range(len(purchases)):
        res.setdefault(purchases[i]['category'], []).append(purchases[i]['price'])
    for key, value in res.items():
        avg[key] = sum(value) / len(value)
    print(f'Средняя цена по категориям: {avg}')
    
#5. Категория с наибольшим числом проданных товаров
def most_frequent_category(purchases):
    return -purchases['quantity'] 

#Исходные данные
purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

#1
total_revenue(purchases)

#2
items_by_category(purchases)

#3
expensive_purchases(purchases, 1.0)

#4
average_price_by_category(purchases)

#5
sorted_most_frequent_category = sorted(purchases, key=most_frequent_category)
print(f'Категория с наибольшим количеством проданных товаров: {sorted_most_frequent_category[0]['category']}')
