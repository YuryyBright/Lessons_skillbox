#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


def task_1():
    # Есть значение радиуса круга
    radius = 42

    # Выведите на консоль значение площади этого круга с точностю до 4-х знаков после запятой
    # подсказки:
    #       формулу можно подсмотреть в интернете,
    #       пи возьмите равным 3.1415926
    #       точность указывается в функции round()
    # TODO здесь ваш код
    print(f"площадь круга радиусом {radius} см с точностю до 4-х знаков после запятой")

    # Далее, пусть есть координаты точки
    point = (24, 34)
    point_2 = (40, 40)
    pi = 3.1415926
    # point for cyrcle 0 0
    # где 23 - координата х, 34 - координата у

    # Если точка point лежит внутри того самого круга (radius = 42), то выведите на консоль True,
    # Или False, если точка лежит во вне круга.
    # подсказки:
    #       нужно определить расстояние от этой точки до начала координат (0, 0)
    #       формула так же есть в интернете
    #       квадратный корень - это возведение в степень 0.5
    #       операции сравнения дают булевы константы True и False
    # TODO здесь ваш код
    print('S =', round(pi * radius ** 2, 4), 'см2')
    # Аналогично для другой точки
    create_plot(radius, point)
    print(point[0] ** 2 + point[1] ** 2 <= radius ** 2)
    print(point_2[0] ** 2 + point_2[1] ** 2 <= radius ** 2)
    # Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
    # Или False, если точка лежит вовне круга.
    # TODO здесь ваш код
    create_plot(radius, point_2)



def create_plot(radius, point):
    ax = plt.gca()
    # Массивы x, y
    theta = np.linspace(0, 2 * np.pi, 100)
    r = 6
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    # change default range so that new circles will work

    ax.set_xlim((0, 10))
    ax.set_ylim((0, 10))
    ax.plot(x, y)
    ax.plot((point[0]), (point[1]), 'o', color='g')

    plt.axis('scaled')
    plt.show()
