#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['мама', 'папа','сестра','бабушка']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ["Lena", 163],
    ["Vasya",173],
    ['Anna', 93],
    ['Nadya', 165],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
def task_4():
    print(" TASK 4")
    summury_height = 0
    for i in range(4):
        print('Height my ',my_family[i],' = ',my_family_height[i][1])
        summury_height += my_family_height[i][1]
    print('summury_height = ',summury_height)