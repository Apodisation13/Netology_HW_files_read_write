from cook_book import cook_book_init


def get_shop_list_by_dishes(dishes: list, person_count: int, cook: dict):
    d = {}
    for dish in dishes:
        if dish in cook:
            for ingredient in cook[dish]:
                # print(ingredient)
                if ingredient['ingredient_name'] not in d:
                    d[ingredient['ingredient_name']] = \
                        {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
                else:
                    quantity = d[ingredient['ingredient_name']]['quantity']
                    d[ingredient['ingredient_name']] = \
                        {'measure': ingredient['measure'],
                         'quantity': (ingredient['quantity'] * person_count) + quantity}
        else:
            print(f'Ошибка: нельзя добавить блюдо {dish}. Оно отсутствует в книге')
    print(d)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book_init())
get_shop_list_by_dishes(["Омлет", "Фахитос"], 3, cook_book_init())
# для этой комбинации повторяется помидор, поэтому его вышло 12: 2*3 + 2*3
get_shop_list_by_dishes(['Утка по-пекински', 'Омлетт'], 2, cook_book_init())
# утку посчитает, а во втором элементе ошибка
