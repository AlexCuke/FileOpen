import pprint

cook_book = {}
# Задание 1 версия 2
def load_cook_book(filename: str) -> dict:
    with open(filename, encoding='utf-8') as file:
        content = file.read().strip()  # читаем весь файл строкой
    blocks = content.split('\n\n') # делим файл на блоки по пустым строкам между рецептами
    for block in blocks:
        lines = block.split('\n')
        dish = lines[0].strip()          
        count = int(lines[1].strip())   
        ingredients = []
        for line in lines[2:2 + count]:
            ing, qty, unit = line.split(' | ')
            ingredients.append({
                'ingredient_name': ing,
                'quantity': int(qty),
                'measure': unit
            })
        cook_book[dish] = ingredients

    return cook_book
cook_book = load_cook_book('cook_book.txt')    
pprint.pprint(cook_book)

# Задание 2 
def get_shop_list_by_dishes(dishes, person_count):
    all_ingr={}
    for dish in dishes:
        if dish in cook_book:
            for ingridient in cook_book[dish]:
                name=ingridient['ingredient_name']
                quantity=ingridient['quantity']*person_count
                measure=ingridient['measure']
                if name in all_ingr:   #добавляем количество к существующему ингридиенту                     
                    all_ingr[name]['quantity'] += quantity 
                else: #создаем новую запись
                    all_ingr[name]={   # 
                        'quantity': quantity,
                        'measure': measure  
                        }        
    pprint.pprint(all_ingr)

get_shop_list_by_dishes(['Омлет','Салат Оливье'], 2)

# Задание 3 
new_files=[['1.txt'],['2.txt'],['3.txt']]
for new_file  in new_files:
    filename=new_file[0]
    with open(filename, encoding='utf-8') as f:
        lines=f.readlines()
    count=len(lines)
    new_file.insert(1,count)

    for line in lines:
            new_file.append(line.strip())
new_files.sort(key=lambda x: x[1])

pprint.pprint(new_files) # тест списка

with open('new.txt', 'w', encoding='utf-8') as out: # записываем в файл
    for file_info in new_files:
        filename = file_info[0]
        count = str(file_info[1])
        lines = file_info[2:]
        out.write(filename + '\n')
        out.write(count + '\n')
        for line in lines:
            out.write(line + '\n')