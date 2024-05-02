import os
import csv


class MyClass:
    """Инициализация переменных"""

    def __init__(self):
        self.path = 0
        self.dict_reader = []
        self.list_dicts = []
        self.sorted_list_int = []
        self.sorted_list_str = []
        self.sorted_list_if = []

    """Подсчёт файлов в заданном пути"""

    def count_files(self):
        self.path = len([name for name in os.listdir('/StudyULGTU/Практика зима') if
                         os.path.isfile(os.path.join('/StudyULGTU/Практика зима', name))])

        print(f'Количество файлов в папке: {self.path}')

    """Запись данных в массив словарей"""

    def write_dict(self):
        with open("data.csv", "r") as f:
            dict_reader = csv.DictReader(f)
            for item in dict_reader:
                self.list_dicts.append(dict(item))

            for item in self.list_dicts:
                for key, value in item.items():
                    try:
                        item[key] = float(value)
                    except ValueError:
                        item[key] = value

    """Функция для сортировки словарей по строчному значению ключа"""

    def sort_by_string(self):
        self.sorted_list_str = sorted(self.list_dicts, key=lambda x: x['day'])
        for i in self.sorted_list_str:
            yield i

    """Функция для сортировки словарей по числовому значению ключа"""

    def sort_by_int(self):
        self.sorted_list_int = sorted(self.list_dicts, key=lambda x: x['width'])
        for i in self.sorted_list_int:
            yield i

    """Функция для сортировки словарей по определённому условию"""

    def sort_by_if(self):
        self.sorted_list_if = [item for item in self.list_dicts if item['length'] > 200]
        for i in self.sorted_list_if:
            yield i

    def print_lst(self):
        for i in self.sort_by_if():
            print(i)

    """Запись результирующих данных в файл"""

    def write_data_file(self):
        with open("output.csv", mode="w", encoding='utf-8') as w_file:
            names = ["number", "latitude", "longitude", "width", "length", "rainfall", "date", "time", "day"]
            file_writer = csv.DictWriter(w_file, delimiter=",",
                                         lineterminator="\r", fieldnames=names)
            file_writer.writeheader()
            for item in self.sorted_list_int:
                file_writer.writerow(item)


class InheritedClass(MyClass):
    def __init__(self):
        super().__init__()


SecondClass = InheritedClass()
SecondClass.write_dict()
SecondClass.print_lst()
