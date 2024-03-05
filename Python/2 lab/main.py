# Поиск корней методом секущих
# Выполнил Попов Ю.А. ИУ7-22Б
# ЛР2

import math
# from collections import


def get_func(func, x0, x1, n_max, eps):
    x, x_prev, i = x0, x1, 0
    flag = True
    while abs(x - x_prev) >= eps and i < n_max:
        x, x_prev, i = x - func(x) / (func(x) - func(x_prev)) * (x - x_prev), x, i + 1
        if i >= n_max:
            flag = False

    if flag:
        return x
    else:
        return  -10000000

    # i += 1


# y = func(x)
# if abs(y) < eps:
#    return x, y, 1
# return x, y, 0


def const_input(EPS) -> tuple:
    flag = True
    a, b, h = float, float, float
    while flag:
        try:
            a = float(input(">>Введите начало отрезка: "))
            b = float(input(">>Введите конец отрезка: "))
            h = float(input(">>Введите шаг разбиения: "))
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


def main():
    N_MAX = 50
    EPS = 10 ** -5
    FUNC = lambda x: math.sin(x)
    a, b, h = const_input(EPS)
    n = math.ceil((b - a) / h)

    for i in range(1, n + 1):
        x0 = a + h * (i - 1)
        x1 = a + h * i
        res = get_func(FUNC, x0, x1, N_MAX, EPS)
        print(res, FUNC(res), x0, x1)


if __name__ == "__main__":
    main()
