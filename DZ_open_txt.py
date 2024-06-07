import os
#1 Задача
with open('test.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        recepie_name = i.strip()
        ingredients_count = file.readline()
        ingredients = []
        for _ in range(int(ingredients_count)):
            recepie = file.readline().strip().split(' | ')
            product, quantity, measure = recepie
            ingredients.append({'product': product, 'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book[recepie_name] = ingredients
        
#2 Задача
def get_shop_list_by_dishes(person_count: int, dishes: dict):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['product'] in result:
                    result[consist['product']]['quantity'] += int(consist['quantity']) * person_count
                else:
                    result[consist['product']] = {'measure': consist['measure'],'quantity': int(consist['quantity' ])* person_count}
        else:
            print(f'Такого блюда нет в книге: {dish}')
          
    print(result)
get_shop_list_by_dishes(3, {'Филадельфия', 'Фахитос','Омлет'})
       
# 3 Задача
def str_count(path_in,out_file:str):
    file_name_count=[]
    line_count=[]
    for root, dirs, files in os.walk(path_in):  
        for file_name in files:
            line_sum = sum(1 for line in open(root+'/'+file_name, encoding='utf-8') )
            file_name_count.append([line_sum,file_name,""])
            line_count.append(line_sum)
            
        for file_list in sorted(file_name_count):
            opening_files = open(out_file, 'a',encoding='utf-8')
            opening_files.write(f'{file_list[1]}\n' )
            opening_files.write(f'{file_list[0]}\n' )
            with open(root+'/'+file_list[1], 'r',encoding='utf-8') as file:
                counting = 1
                for line in file:
                    opening_files.write(f'строка № {counting} в файле {file_list[1].split(".")[0]} \n')
                    counting += 1
                    print(line)
            opening_files.write(f'\n')
            opening_files.close()
path_in = "C:\\Users\\Den\\Documents\\Homework1\\test"
out_file = "out.txt"  
str_count(path_in,out_file)