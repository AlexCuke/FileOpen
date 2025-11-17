import pprint
'''
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
'''
# Задание 3 
new_file=[]
new_files=[['1.txt'],['2.txt'],['3.txt']]
for new_file in new_files:

    with open(new_file[0], encoding='utf-8') as file:
        count_string=0
        while True:
            line = file.readline().strip()
            new_file.append(line)
            if not line:
                break
            count_string +=1  # счетчик строк
        #print(count_string)
        new_file.insert(1,count_string)
    print(new_file)
print()
i=0
for i in range (len(new_files)-1):
    if new_files[i][1]>new_files[i+1][1]:
            spis=new_files[i]
            new_files[i]=new_files[i+1]
            new_files[i+1]=spis

pprint.pprint(new_files)

for new_file in new_files:
     new_file[1]=str(new_file[1])


with open('new.txt', 'w', encoding='utf-8') as file:
    for new_file in new_files:
        file.writelines([line + '\n' for line in new_file[:]])