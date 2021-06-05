#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

# TODO здесь ваш код
def task_3():
    print(" TASK 3")
    print('string = ', my_favorite_movies)
    print('первый фильм')
    print(my_favorite_movies[0:10])
    print('последний фильм')
    print(my_favorite_movies[-15:])
    print('второй')
    print(my_favorite_movies[12:25])
    print('второй с конца')
    print(my_favorite_movies[-22:-17])
