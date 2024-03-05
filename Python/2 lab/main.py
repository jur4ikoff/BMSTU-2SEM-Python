# Поиск корней методом секущих
# Выполнил Попов Ю.А. ИУ7-22Б
# ЛР2

import math
from utils import input_number
import numpy as np
from matplotlib import pyplot as plt

N_MAX = 50
EPS = 10 ** -5
FUNC = lambda x: math.sin(x)


def secant_method(f, a, b, eps, Nmax) -> tuple:
    if f(a) * f(b) > 0:
        return None, -1, 1

    x0 = a
    x1 = b
    n = 1

    while abs(f(x1)) > eps and n < Nmax:
        x_next = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        x0 = x1
        x1 = x_next
        n += 1

    if n == Nmax:
        return None, n, 2
    else:
        return x1, n, 0


def const_input(EPS) -> tuple:
    flag = True
    a, b, h = float, float, float
    while flag:
        try:
            a = input_number(">>Введите начало отрезка", float)
            b = input_number(">>Введите конец отрезка", float)
            h = input_number(">>Введите шаг разбиения", float)
        except ValueError as e:
            print(f"{e}, Wrong Input")
            continue

        if a >= b:
            print("Error: B must be bigger then A (b < a)")
        elif h < EPS:
            print("Error: h must be bigger then EPS")
        elif h < 0:
            print("Error: h must be Positive")
        else:
            flag = False

    return a, b, h


def make_table(table):
    print()
    print(f"{'Таблица корней':^107}")
    print('—' * 107)
    print(f"|{'№ корня':^10}|{'интервал':^25}|{'x':^20}|{'f(x)':^20}|{'Iteration count':^15}|{'Error Code':^10}|")
    print('—' * 107)

    for i in range(len(table)):
        print(
            f"|{table[i][0]:^10}|{f'[{table[i][1][0]:^6.6g};{table[i][1][1]:^6.6g}]':^25}|{table[i][2]:^20.7g}|{table[i][3]:^20.7g}|{table[i][4]:^15}|{table[i][5]:^10}|")
    print('—' * 107)

    return ""

def find_extremums(x_axis: list, y_axis: list) -> list:
    extremums = []
    for i in range(1, len(x_axis) - 1):
        if y_axis[i - 1] < y_axis[i] and y_axis[i] > y_axis[i + 1]:
            extremums.append((x_axis[i], y_axis[i]))
        elif y_axis[i - 1] > y_axis[i] and y_axis[i] < y_axis[i + 1]:
            extremums.append((x_axis[i], y_axis[i]))

    return extremums


def find_inflection_points(x_axis: list, y_axis: list) -> list:
    inflection_points = []
    for i in range(2, len(y_axis) - 2):
        if (y_axis[i] - 2 * y_axis[i - 1] + y_axis[i - 2]) * (
            y_axis[i] - 2 * y_axis[i + 1] + y_axis[i + 2]
        ) < 0:  # Проверяем условие точки перегиба
            inflection_points.append((x_axis[i], y_axis[i]))

    return inflection_points

def create_graph(f, x, result):

    y = list(map(f, x))
    plt.plot(x, y)
    plt.title('График функции')
    plt.xlabel('x')
    plt.ylabel('f(x)')

    extremums = find_extremums(x, y)
    inflections = find_inflection_points(x, y)

    plt.scatter(*zip(*extremums), color='red', label='Extremum')
    plt.scatter(*zip(*inflections), color='green', label='Inflection point')
    plt.scatter(*zip(*[[el[2], el[3]] for el in result]), color='blue', label='Solution')

    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    result = []
    a, b, h = const_input(EPS)
    n = math.ceil((b - a) / h)

    for i in range(1, n + 1):
        x0 = a + h * (i - 1)
        x1 = a + h * i
        res, iterations, exit_code = secant_method(FUNC, x0, x1, EPS, N_MAX)
        # if n > 50:
        if isinstance(res, (float, int)):
            result.append([i, (x0, x1), res, FUNC(res), iterations, exit_code])
        # else:
        # if isinstance(res, (float, int)):
        #    result.append([i, (x0, x1), res, FUNC(res), iterations, exit_code])
        # else:
        # result.append([i, (x0, x1), '-', '-', iterations, exit_code])

    make_table(result)
    create_graph(FUNC, np.linspace(a, b, n), result)


if __name__ == "__main__":
    main()
