import pprint
cook_book = {}
# Задание 1
with open('cook_book.txt', encoding='utf-8') as file:
    while True:
        dish = file.readline().strip()
        if not dish:
            break
        count = int(file.readline())  # сколько ингредиентов будет
        ingredients = []
        for _ in range(count):
            line = file.readline().strip()
            ing, qty, unit = line.split(' | ')
            ingredients.append({
                'ingredient_name': ing,
                'quantity': int(qty),
                'measure': unit
            })
        cook_book[dish] = ingredients
        file.readline()  # пропускаем пустую строку между рецептами

#pprint.pprint(cook_book)


# Задание 2
def get_shop_list_by_dishes(dishes, person_count):
    all_ingr={}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in all_ingr:
                    key=all_ingr.get(ingredient['ingredient_name'], ingredient['quantity'] * person_count)
                    all_ingr[ingredient['ingredient_name']] = ingredient['quantity'] * person_count + key
                else:
                    all_ingr.setdefault(ingredient['ingredient_name'], ingredient['quantity'] * person_count)
    print(all_ingr)
dishes=['Омлет','Салат Оливье']
person_count=2

get_shop_list_by_dishes(dishes, person_count)

