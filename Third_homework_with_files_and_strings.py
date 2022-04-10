# 1) Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них
# (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
# 2) Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем
# Итоговый файл:
# 2.txt
# 1
# Строка номер 1 файла номер 2
# 1.txt
# 2
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1

def who_is_who(files=[]):
    unsorted_dict_for_who_fuction = {}
    for file in files:
        file_name=file
        with open(file, encoding="utf-8") as file:
            data = file.read()
            strings = data.count('\n')+1
            unsorted_dict_for_who_fuction[file_name]=strings
    return unsorted_dict_for_who_fuction
print(who_is_who(['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']).items())

unsorted_dict = who_is_who(['1.txt', '2.txt', '3.txt', '4.txt', '5.txt'])

def sorting(dict_to_sort):
    sorted_dict_for_sorting_function = {}
    amount_of_files = len(dict_to_sort)
    print(amount_of_files)
    list_of_all_strings_amount_unsorted = []
    for strings_amount in dict_to_sort.values():
        list_of_all_strings_amount_unsorted.append(strings_amount)
    # print(list_of_all_strings_amount_unsorted)
    list_of_all_strings_amount_sorted = sorted(list_of_all_strings_amount_unsorted)
    # print(list_of_all_strings_amount_sorted)

    counter=1
    for sorted_order_of_strings in list_of_all_strings_amount_sorted:
        dict_for_import = {}
        for file_name, strings_amount in dict_to_sort.items():
            if sorted_order_of_strings == strings_amount:
                dict_for_import[file_name]=strings_amount
                sorted_dict_for_sorting_function[counter]=dict_for_import
        counter +=1
    print(sorted_dict_for_sorting_function.items())
    return(sorted_dict_for_sorting_function)

sorted_dict = sorting(unsorted_dict)

def result (sorted_dict_for_resulting_file, total_file_name):
    with open(total_file_name, 'a', encoding="utf-8") as file:
        for dict_with_name_and_strings_amount in sorted_dict_for_resulting_file.values():
            for name, strings_amount in dict_with_name_and_strings_amount.items():
                file.write(name)
                file.write('\n')
                strings_amount = str(strings_amount)
                file.write(strings_amount)
                file.write('\n')
                with open(name, encoding="utf-8") as file2:
                    data=file2.read()
                    file.write(data)
                    file.write('\n\n')

result (sorted_dict, 'x.txt')
