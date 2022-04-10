def strings_amount(file):
    with open(file, encoding="utf-8") as file:
        data = file.read()
        strings = data.count('\n')
        return strings
def dishes_amount(file):
    with open(file, encoding="utf-8") as file:
        data = file.readlines()
        dishes = data.count('\n')
        return dishes
print("-----")
print(f"Количество строк в файле {strings_amount('recipe.txt')}")
print(f"Количество блюд в файле {dishes_amount('recipe.txt')}")

cook_book={}
print("-----")

def dictionary(file, strings):
    with open(file, encoding="utf-8") as file:
        string_counter = 1
        list_of_dicts = []
        dict_in_dict = {}
        temp_list = []
        for string in range(strings):
            data = file.readline().strip()
            if string_counter == 1:
                cook_book[data] = {}
                string_counter += 1
                header = data
            elif string_counter == 2:
                string_counter += 1
            elif data !="":
                splitted_string = data.split("|")
                ingredient_counter = 0
                for item in splitted_string:
                    ingredient_counter += 1
                    if item[-1] == " ":
                        item = item[:-1]
                        # print(item)
                    elif item[0] == " ":
                        item = item[1:]
                    if ingredient_counter == 1:
                        dict_in_dict['ingredient_name'] = item
                    elif ingredient_counter == 2:
                        dict_in_dict['quantity'] = item
                    elif ingredient_counter == 3:
                        dict_in_dict['measure'] = item
                        temp_dict = dict_in_dict.copy()
                        list_of_dicts.append(temp_dict)
                        dict_in_dict.clear()
                        temp_list = list_of_dicts.copy()
                        cook_book[header] = temp_list
                    string_counter += 1

            elif data =="":
                list_of_dicts.clear()
                string_counter = 1

dictionary('recipe.txt', strings_amount('recipe.txt'))

shop_list={}
def get_shop_list_by_dishes (dishes, person_count):
    for dish in dishes:
        # print(dish)
        if dish not in cook_book.keys():
            print(f"Такого блюда, как {dish} в повареной книге нет")
        for ingredient in cook_book.get(dish):
            # print(ingredient)
            ingredient_string = {}
            counter = 1
            # Все что в цикле FOR ниже - происходит внутри строки ингредиента
            for english, after_english in ingredient.items():
                # print(f"Англоключ <{english}> | Значение <{after_english}>")
                if counter ==1: # 1 - название игредиента в строке(словаре)
                    duplicate_flag = 0
                    after_english = after_english
                    if after_english in shop_list.keys():
                        duplicate_flag = 1
                        dict_for_magic = shop_list.get(after_english)
                        remembered_quality = dict_for_magic.get('quantity')
                    elif after_english not in shop_list.keys():
                        shop_list[after_english] = ingredient_string
                if counter ==2: # 2 - количество
                    after_english = int(after_english)
                    after_english *= person_count
                    if duplicate_flag !=1:
                        ingredient_string[english]=after_english
                    else:
                        sum_of_amount = after_english + remembered_quality
                        ingredient_string[english] = sum_of_amount
                        # print(f" Суммируемое количество {sum_of_amount}")
                        # print(f" Значение количества в закладываемом элементе {ingredient_string.get(english)}")
                        # print(f" Значения словаря {shop_list.values()}")
                        # shop_list[after_english] = ingredient_string
                if counter ==3: # 3 - измерение
                    ingredient_string[english]=after_english
                    # print(f" Значение количества в закладываемом элементе {ingredient_string.get(english)}")
                    duplicate_flag = 0
                counter +=1

get_shop_list_by_dishes(["Утка по-пекински", "Утка по-пекински"], 1)

for ingredient, amount in shop_list.items():
    print(ingredient, amount)
