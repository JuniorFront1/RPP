import numpy as np


# функция ввода элемента и проверка на коррекцию ввода
def take_number():
    while True:
        try:
            number = int(input('Введите число: '))
        except ValueError:
            print('Нужно ввести число!')
        else:
            return number


# инициализая 2х мерного массива при помощи рандом функции
def init_2d_array(n, m):
    my_list = np.random.randint(-10, 10, size=(n, m))
    return my_list


# поиск введённого элемента в 2х мерной матрице и вывод столбца, в котором есть данный элемент
def action_2d_array():
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            if my_list[i][j] == h:
                print(f'{h} найдено в столбце:', j)
                print()


# вывод в консоль 2х мерного массива
def print_2d_array():
    for subarr in my_list:
        print(*subarr, end='\n')


# вывод в файл 2х мерного массива
def print_in_file_2d_array():
    context_file = open('outputRPP(2).txt', mode='wt')
    for subarr in my_list:
        print(*subarr, sep=' ', file=context_file)


h = take_number()
my_list = init_2d_array(100, 100)
print_2d_array()
print()
action_2d_array()
print_in_file_2d_array()
