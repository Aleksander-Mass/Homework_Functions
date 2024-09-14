"""
Домашняя работа по уроку "Функции в Python.Функция с параметром"

Задача "Матрица воплоти":

Напишите функцию get_matrix с тремя параметрами n, m и value, которая будет создавать матрицу(вложенный список)
размерами n строк и m столбцов, заполненную значениями value и возвращать эту матрицу в качестве результата работы.
"""

"""
Пункты задачи:

Объявите функцию get_matrix и напишите в ней параметры n, m и value.
Создайте пустой список matrix внутри функции get_matrix.
Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
В первом цикле добавляйте пустой список в список matrix.
Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
Во втором цикле пополняйте ранее добавленный пустой список значениями value.
После всех циклов верните значение переменной matrix.
Выведите на экран(консоль) результат работы функции get_matrix.
"""

# 1. Объявите функцию get_matrix и напишите в ней параметры n, m и value:

def get_matrix (n, m, value):
    matrix = [] # 2. Создайте пустой список matrix внутри функции get_matrix

    # 3. Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов:

    for i in range(n):
        matrix.append([]) # 4. В первом цикле добавляйте пустой список в список matrix

        # 5. Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов:
        for j in range(m):

            # 6. Во втором цикле пополняйте ранее добавленный пустой список значениями value:
            matrix[i].append(value) # Пишем в список значение

    # После всех циклов верните значение переменной matrix:
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)




