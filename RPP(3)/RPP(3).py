import os
import csv

# 1 пункт задания --------------------------------------------------------------------------------
# Получение количества файлов через конкатенацию строк библиотеки os при помощи метода .path.join
path = len([name for name in os.listdir('/StudyULGTU/Практика зима') if
            os.path.isfile(os.path.join('/StudyULGTU/Практика зима', name))])
print(f'Количество файлов в папке: {path}')

# 2 пункт задания --------------------------------------------------------------------------------


with open("data.csv", "r") as f:
    dict_reader = csv.DictReader(f)
    list_dicts = []
    for item in dict_reader:
        list_dicts.append(dict(item))

    for item in list_dicts:
        for key, value in item.items():
            try:
                item[key] = float(value)
            except ValueError:
                item[key] = str(value)

    # Сортировка по числовому значению ключа
    sorted_list_int = sorted(list_dicts, key=lambda x: x['length'])

    # Сортировка по строковому значению ключа
    sorted_list_str = sorted(list_dicts, key=lambda x: x['day'])

    # Сортировка по определённому условию
    sorted_list_if = [item for item in list_dicts if item['length'] > 200]

    print(sorted_list_int)

with open("output.csv", mode="w", encoding='utf-8') as w_file:
    names = ["number", "latitude", "longitude", "width", "length", "rainfall", "date", "time", "day"]
    file_writer = csv.DictWriter(w_file, delimiter=",",
                                 lineterminator="\r", fieldnames=names)
    file_writer.writeheader()
    for item in sorted_list_int:
        file_writer.writerow(item)



