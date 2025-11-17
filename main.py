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
            for ingridient in cook_book[dish]:
                kol=ingridient['quantity'] * person_count
                ingr1={}
                if ingridient['ingredient_name'] in all_ingr:
                    key=ingr1.setdefault('quantity', kol)
                    kol=key+kol
                    ingr1.setdefault('measure', ingridient['measure'] )
                    ingr1['quantity'] = (kol)
                    all_ingr[ingridient['ingredient_name']] = ingr1
                else:
                    ingr1.setdefault('quantity', kol)  
                    ingr1.setdefault('measure', ingridient['measure'] )
                    all_ingr.setdefault(ingridient['ingredient_name'], ingr1)              
    pprint.pprint(all_ingr)

dishes=['Омлет','Салат Оливье']
person_count=2

get_shop_list_by_dishes(dishes, person_count)
