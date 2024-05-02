# Импортируем библиотеку для генерации случайных чисел
import random

#ЫвВЫФВФ
# Класс, в котором будут хранится методы, используемые для работы над списком (заполнение и проверка на ошибки)
class MyClass:

    def checkElementsOfList(self, isGenerate, len_array):
        # Проверка на генерацию списка при помощи случайных чисел
        if isGenerate:
            # Метод sample возвращает готовый список элементов по заданным параметрам
            # В нашем случае это числа от -100 до 100 (101 не включается) и с заданной длинной списка
            numbers_list = random.sample(range(-100, 101), len_array)

            # Сообщаем пользователю о успешной генерации списка
            print('List is automatically generated!')
            # Возвращаем результирующий список элементов
            return numbers_list

        # Присваиваем в переменную введённый список элементов при помощи клавиатуры и с помощью
        # метода .split() возвращаем список строк, разделённых пробелом

        # Переводим каждый элемент в целое число и записываем результат в переменную
        while True:
            try:
                numbers_string = input('Enter items of list: ').split()
                numbers_list = [int(i) for i in numbers_string]
            except ValueError:
                print('Нельзя вводить строки!')
            else:
                # Возвращаем результирующий список элементов
                return numbers_list

    # Метод по нахождению индекса минимального элемента, путём сравнения в цикле
    def findMinItem(self, numbers_list, len_array):
        min_item = numbers_list[0]
        min_index = 0
        for i in range(len_array):
            if numbers_list[i] < min_item:
                min_index = i
                min_item = numbers_list[i]

        return min_index

    # Метод по нахождению индекса максимального элемента, путём сравнения в цикле
    def findMaxItem(self, numbers_list, len_array):
        max_item = numbers_list[0]
        max_index = 0
        for i in range(len_array):
            if numbers_list[i] > max_item:
                max_index = i
                max_item = numbers_list[i]

        return max_index

    # Метод по нахождению и удалению чётных элементов между индексом минимального и максимального элемента
    def deleteItems(self, numbers_list, min_index, max_index):
        # Проверка позиций минимального и максимального индекса и запись в соответсвующие переменные
        if min_index > max_index:
            first_index = max_index
            second_index = min_index
        else:
            first_index = min_index
            second_index = max_index

        # Перебор элементов массива и удаление чётных при помощи метода .pop(), в который передаётся индекс элемента
        for i in range(first_index + 1, second_index):
            if numbers_list[i] % 2 == 0:
                numbers_list[i] = -101

        result_list = [int(i) for i in numbers_list if i != -101]

        return result_list

    # Альтернативные методы

    def alternativeFindMinItem(self, numbers_list):
        min_index = numbers_list.index(min(numbers_list))

        return min_index

    def alternativeFindMaxItem(self, numbers_list):
        max_index = numbers_list.index(max(numbers_list))

        return max_index

    def alternativeDeleteItems(self, numbers_list, min_index, max_index):
        if min_index > max_index:
            first_index = max_index
            second_index = min_index
        else:
            first_index = min_index
            second_index = max_index

        for i in range(second_index - 1, first_index, -1):
            if numbers_list[i] % 2 == 0:
                numbers_list.pop(i)

        return numbers_list


ListItems = MyClass()
size_array = int(input('Enter size of array: '))
numbers_list = ListItems.checkElementsOfList(1, size_array)
print(numbers_list)

# Альтернативные методы
# min_indx = ListItems.alternativeFindMinItem(numbers_list)
# max_indx = ListItems.alternativeFindMaxItem(numbers_list)
# print(f'Min index:{min_indx}', f'\nMax index:{max_indx}')
# print(ListItems.deleteItems(numbers_list, min_indx, max_indx))

min_indx = ListItems.findMinItem(numbers_list, size_array)
max_indx = ListItems.findMaxItem(numbers_list, size_array)
print(f'Min index:{min_indx}', f'\nMax index:{max_indx}')
print(ListItems.deleteItems(numbers_list, min_indx, max_indx))
